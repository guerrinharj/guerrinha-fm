from django.core.management.base import BaseCommand
from tracks.models import Track

class Command(BaseCommand):
    help = 'Seed the database with a test track'

    def handle(self, *args, **kwargs):
        Track.objects.all().delete()

        Track.objects.create(
            name="Chalé",
            album="Wagner",
            year=2018,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Wagner/Guerrinha%20-%20Wagner%20-%2001%20Chale%CC%81.mp3",
            album_url="https://www.gpgc.info/releases/wagner",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Wagner/cover.png"
        )

        self.stdout.write(self.style.SUCCESS("✅ Database seeded with track 'Chalé'"))
