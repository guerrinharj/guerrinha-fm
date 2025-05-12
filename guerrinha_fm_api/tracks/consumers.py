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
        await self.channel_layer.group_add("radio", self.channel_name)
        await self.accept()

        try:
            while True:
                track = await self.get_now_playing()
                print("🎵 Got track:", track)

                if track:
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
                    print("📤 Sending:", response)
                    await self.send(text_data=json.dumps(response))

                    # Get MP3 duration from URL
                    duration = await self.get_mp3_duration(track.song_url)
                    print(f"⏳ Waiting {duration} seconds until next track...")
                    await asyncio.sleep(duration)
                else:
                    print("⚠️ No track found.")
                    await asyncio.sleep(5)
        except Exception as e:
            print("❌ Exception during connect():", repr(e))
            await self.close(code=1000)  # WebSocket close code (1000 = normal)

    async def disconnect(self, close_code):
        print(f"📴 Disconnected with code: {close_code}")
        await self.channel_layer.group_discard("radio", self.channel_name)

    @sync_to_async
    def get_now_playing(self):
        print("🔍 Picking a random track...")
        return Track.objects.order_by("?").first()

    @sync_to_async
    def get_mp3_duration(self, url):
        try:
            print("📡 Fetching MP3 from:", url)
            response = requests.get(url, stream=True)
            response.raise_for_status()

            chunk = response.raw.read(1024 * 500)  # Read first ~500KB
            audio = MP3(BytesIO(chunk))
            duration = int(audio.info.length)
            print(f"🎚️ MP3 duration: {duration}s")
            return duration
        except Exception as e:
            print("⚠️ Failed to get duration, defaulting to 10s:", e)
            return 10  # Fallback
