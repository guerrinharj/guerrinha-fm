import json
from channels.generic.websocket import AsyncWebsocketConsumer
from tracks.models import Track
from asgiref.sync import sync_to_async
from django.utils.timezone import now

class RadioConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("📡 WebSocket client connected")
        await self.channel_layer.group_add("radio", self.channel_name)
        await self.accept()

        track = await self.get_now_playing()

        if track:
            await self.send(text_data=json.dumps({
                "track": {
                    "name": track.name,
                    "album": track.album,
                    "year": track.year,
                    "url": track.song_url,
                    "album_url": track.album_url,
                    "cover_url": track.cover_url,
                    "start_time": now().isoformat()
                }
            }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("radio", self.channel_name)

    @sync_to_async
    def get_now_playing(self):
        return Track.objects.first()
