import asyncio
import json
import requests
import redis

from io import BytesIO
from mutagen.mp3 import MP3

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync, sync_to_async
from django.core.management.base import BaseCommand
from tracks.models import Track
from django.utils.timezone import now

class Command(BaseCommand):
    help = "Start the radio broadcast loop"
    
    now_playing = None

    def handle(self, *args, **options):
        async_to_sync(self.broadcast_loop)()

    async def broadcast_loop(self):
        channel_layer = get_channel_layer()

        while True:
            track = await self.get_random_track()
            if not track:
                await asyncio.sleep(5)
                continue

            duration = await self.get_mp3_duration(track.song_url)

            response = {
                "track": {
                    "name": track.name,
                    "album": track.album,
                    "year": track.year,
                    "url": track.song_url,
                    "duration": track.duration,
                    "album_url": track.album_url,
                    "cover_url": track.cover_url,
                    "start_time": now().isoformat()
                }
            }

            r = redis.Redis()
            r.set("now_playing", json.dumps(response))

            Command.now_playing = response

            print("📡 Broadcasting track:", response)

            await channel_layer.group_send("radio", {
                "type": "radio.broadcast",
                "text": json.dumps(response)
            })

            print("✅ group_send finished")

            await asyncio.sleep(duration)

    @sync_to_async
    def get_random_track(self):
        return Track.objects.order_by("?").first()

    async def get_mp3_duration(self, url):
        try:
            response = requests.get(url, stream=True, timeout=5)
            response.raise_for_status()
            chunk = response.raw.read(1024 * 500)
            audio = MP3(BytesIO(chunk))
            return int(audio.info.length)
        except Exception as e:
            print("⚠️ Failed to get duration:", e)
            return 10
