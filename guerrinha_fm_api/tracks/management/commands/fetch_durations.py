import requests
from io import BytesIO
from mutagen.mp3 import MP3

from django.core.management.base import BaseCommand
from tracks.models import Track

class Command(BaseCommand):
    help = "Fetch and store duration for tracks that don't have it"

    def handle(self, *args, **kwargs):
        tracks = Track.objects.filter(duration__isnull=True)

        if not tracks.exists():
            self.stdout.write("✅ All tracks already have durations.")
            return

        for track in tracks:
            try:
                self.stdout.write(f"🎧 Fetching: {track.name}...")
                response = requests.get(track.song_url, stream=True, timeout=5)
                chunk = response.raw.read(1024 * 512)
                audio = MP3(BytesIO(chunk))
                track.duration = int(audio.info.length)
                track.save()
                self.stdout.write(f"✅ {track.name} → {track.duration} seconds")
            except Exception as e:
                self.stderr.write(f"⚠️ Failed: {track.name} → {e}")
