import json
import asyncio
import requests
from io import BytesIO
from mutagen.mp3 import MP3

from channels.generic.websocket import AsyncWebsocketConsumer
from tracks.models import Track
from asgiref.sync import sync_to_async
from django.utils.timezone import now

class RadioConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("📡 WebSocket client connected")
        print("🔌 Channel layer is:", self.channel_layer)
        await self.channel_layer.group_add("radio", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        print(f"📴 Disconnected with code: {close_code}")
        await self.channel_layer.group_discard("radio", self.channel_name)

    async def radio_broadcast(self, event):
        print(f"📥 Receiving broadcast: {event}")
        await self.send(text_data=event["text"])