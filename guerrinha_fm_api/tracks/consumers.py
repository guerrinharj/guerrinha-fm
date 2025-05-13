import json
import redis

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from tracks.models import Track
from django.utils.timezone import now

class RadioConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("📡 WebSocket client connected")
        print("🔌 Channel layer is:", self.channel_layer)

        await self.channel_layer.group_add("radio", self.channel_name)
        await self.accept()

        r = redis.Redis()
        try:
            now_playing = r.get("now_playing")
            if now_playing:
                print("📤 Sending now_playing from Redis")
                await self.send(text_data=now_playing.decode("utf-8"))
        except Exception as e:
            print("⚠️ Redis error:", e)

    async def disconnect(self, close_code):
        print(f"📴 Disconnected with code: {close_code}")
        await self.channel_layer.group_discard("radio", self.channel_name)

    async def radio_broadcast(self, event):
        data = json.loads(event["text"])
        track_name = data.get("track", {}).get("name", "Unknown")
        print(f"📥 Receiving broadcast: {track_name}")
        await self.send(text_data=event["text"])

    @sync_to_async
    def get_now_playing(self):
        from tracks.management.commands.start_radio import Command
        return Command.now_playing
