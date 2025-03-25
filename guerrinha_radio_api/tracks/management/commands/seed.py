from django.core.management.base import BaseCommand
from tracks.models import Track

class Command(BaseCommand):
    help = 'Seed the database with test tracks'

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

        Track.objects.create(
            name="Edifício",
            album="Wagner",
            year=2018,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Wagner/Guerrinha%20-%20Wagner%20-%2002%20Edifi%CC%81cio.mp3",
            album_url="https://www.gpgc.info/releases/wagner",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Wagner/cover.png"
        )

        Track.objects.create(
            name="Gazebo",
            album="Wagner",
            year=2018,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Wagner/Guerrinha%20-%20Wagner%20-%2003%20Gazebo.mp3",
            album_url="https://www.gpgc.info/releases/wagner",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Wagner/cover.png"
        )

        Track.objects.create(
            name="Rancho",
            album="Wagner",
            year=2018,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Wagner/Guerrinha%20-%20Wagner%20-%2004%20Rancho.mp3",
            album_url="https://www.gpgc.info/releases/wagner",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Wagner/cover.png"
        )

        Track.objects.create(
            name="Auditório",
            album="Wagner",
            year=2018,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Wagner/Guerrinha%20-%20Wagner%20-%2005%20Audito%CC%81rio.mp3",
            album_url="https://www.gpgc.info/releases/wagner",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Wagner/cover.png"
        )

        Track.objects.create(
            name="Mirante",
            album="Wagner",
            year=2018,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Wagner/Guerrinha%20-%20Wagner%20-%2006%20Mirante.mp3",
            album_url="https://www.gpgc.info/releases/wagner",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Wagner/cover.png"
        )

        Track.objects.create(
            name="Bosque",
            album="Wagner",
            year=2018,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Wagner/Guerrinha%20-%20Wagner%20-%2007%20Bosque.mp3",
            album_url="https://www.gpgc.info/releases/wagner",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Wagner/cover.png"
        )

        Track.objects.create(
            name="Pomar",
            album="Wagner",
            year=2018,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Wagner/Guerrinha%20-%20Wagner%20-%2008%20Pomar.mp3",
            album_url="https://www.gpgc.info/releases/wagner",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Wagner/cover.png"
        )

        self.stdout.write(self.style.SUCCESS("✅ Database seeded with tracks"))
