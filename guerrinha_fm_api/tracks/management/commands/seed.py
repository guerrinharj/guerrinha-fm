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

        Track.objects.create(
            name="Apartamento",
            album="Apartamento",
            year=2019,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Apartamento/Guerrinha%20-%20Apartamento%20-%2001%20Apartamento.mp3",
            album_url="https://www.gpgc.info/releases/apartamento",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Apartamento/cover.jpg"
        )

        Track.objects.create(
            name="Bodega",
            album="Bodega / Docas",
            year=2020,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Bodega%20%3A%20Docas/Guerrinha%20-%20Bodega%20-%20Docas%20-%2001%20Bodega.mp3",
            album_url="https://www.gpgc.info/releases/bodega-docas",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Bodega%20%3A%20Docas/cover.jpg"
        )

        Track.objects.create(
            name="Docas",
            album="Bodega / Docas",
            year=2020,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Bodega%20%3A%20Docas/Guerrinha%20-%20Bodega%20-%20Docas%20-%2002%20Docas.mp3",
            album_url="https://www.gpgc.info/releases/bodega-docas",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Bodega%20%3A%20Docas/cover.jpg"
        )

        Track.objects.create(
            name="Tasca",
            album="Tasca",
            year=2021,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Tasca/Guerrinha%20-%20Tasca%20-%2001%20Tasca.mp3",
            album_url="https://www.gpgc.info/releases/tasca",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Tasca/cover.jpg"
        )

        Track.objects.create(
            name="José, Pt. I",
            album="Cidade Grande",
            year=2022,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Cidade%20Grande/Guerrinha%20-%20Cidade%20Grande%20-%2001%20Jose%CC%81%2C%20Pt.%20I.mp3",
            album_url="https://www.gpgc.info/releases/cidade-grande",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Cidade%20Grande/cover.png"
        )

        Track.objects.create(
            name="Adulto na Cidade Grande",
            album="Cidade Grande",
            year=2022,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Cidade%20Grande/Guerrinha%20-%20Cidade%20Grande%20-%2002%20Adulto%20na%20Cidade%20Grande.mp3",
            album_url="https://www.gpgc.info/releases/cidade-grande",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Cidade%20Grande/cover.png"
        )

        Track.objects.create(
            name="Galeria Obsoleta",
            album="Cidade Grande",
            year=2022,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Cidade%20Grande/Guerrinha%20-%20Cidade%20Grande%20-%2003%20Galeria%20Obsoleta.mp3",
            album_url="https://www.gpgc.info/releases/cidade-grande",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Cidade%20Grande/cover.png"
        )

        Track.objects.create(
            name="Noite Cartunesca",
            album="Cidade Grande",
            year=2022,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Cidade%20Grande/Guerrinha%20-%20Cidade%20Grande%20-%2004%20Noite%20Cartunesca.mp3",
            album_url="https://www.gpgc.info/releases/cidade-grande",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Cidade%20Grande/cover.png"
        )

        Track.objects.create(
            name="Venda Casa Village",
            album="Cidade Grande",
            year=2022,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Cidade%20Grande/Guerrinha%20-%20Cidade%20Grande%20-%2005%20Venda%20Casada%20Village.mp3",
            album_url="https://www.gpgc.info/releases/cidade-grande",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Cidade%20Grande/cover.png"
        )

        Track.objects.create(
            name="Uma Piada Engraçada",
            album="Cidade Grande",
            year=2022,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Cidade%20Grande/Guerrinha%20-%20Cidade%20Grande%20-%2006%20Uma%20Piada%20Engrac%CC%A7ada.mp3",
            album_url="https://www.gpgc.info/releases/cidade-grande",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Cidade%20Grande/cover.png"
        )

        Track.objects.create(
            name="Kafka Hoje",
            album="Cidade Grande",
            year=2022,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Cidade%20Grande/Guerrinha%20-%20Cidade%20Grande%20-%2007%20Kafta%20Hoje.mp3",
            album_url="https://www.gpgc.info/releases/cidade-grande",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Cidade%20Grande/cover.png"
        )

        Track.objects.create(
            name="José, Pt. II",
            album="Cidade Grande",
            year=2022,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Cidade%20Grande/Guerrinha%20-%20Cidade%20Grande%20-%2008%20Jose%CC%81%2C%20Pt.%20II.mp3",
            album_url="https://www.gpgc.info/releases/cidade-grande",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Cidade%20Grande/cover.png"
        )

        Track.objects.create(
            name="Tempo Engordado",
            album="Exposição Popular",
            year=2024,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Exposic%CC%A7a%CC%83o%20Popular/Guerrinha%20-%20Exposic%CC%A7a%CC%83o%20Popular%20-%2001%20Tempo%20Engordado.mp3",
            album_url="https://www.gpgc.info/releases/exposicao-popular",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Exposic%CC%A7a%CC%83o%20Popular/cover.png"
        )

        Track.objects.create(
            name="Boa Definição",
            album="Exposição Popular",
            year=2024,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Exposic%CC%A7a%CC%83o%20Popular/Guerrinha%20-%20Exposic%CC%A7a%CC%83o%20Popular%20-%2002%20Boa%20Definic%CC%A7a%CC%83o.mp3",
            album_url="https://www.gpgc.info/releases/exposicao-popular",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Exposic%CC%A7a%CC%83o%20Popular/cover.png"
        )

        Track.objects.create(
            name="A Sétima Doninha",
            album="Exposição Popular",
            year=2024,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Exposic%CC%A7a%CC%83o%20Popular/Guerrinha%20-%20Exposic%CC%A7a%CC%83o%20Popular%20-%2003%20A%20Se%CC%81tima%20Doninha.mp3",
            album_url="https://www.gpgc.info/releases/exposicao-popular",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Exposic%CC%A7a%CC%83o%20Popular/cover.png"
        )

        Track.objects.create(
            name="Zombeta",
            album="Exposição Popular",
            year=2024,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Exposic%CC%A7a%CC%83o%20Popular/Guerrinha%20-%20Exposic%CC%A7a%CC%83o%20Popular%20-%2004%20Zombeta.mp3",
            album_url="https://www.gpgc.info/releases/exposicao-popular",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Exposic%CC%A7a%CC%83o%20Popular/cover.png"
        )

        Track.objects.create(
            name="Edificio Argentina",
            album="Exposição Popular",
            year=2024,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Exposic%CC%A7a%CC%83o%20Popular/Guerrinha%20-%20Exposic%CC%A7a%CC%83o%20Popular%20-%2005%20Edifi%CC%81cio%20Argentina.mp3",
            album_url="https://www.gpgc.info/releases/exposicao-popular",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Exposic%CC%A7a%CC%83o%20Popular/cover.png"
        )

        Track.objects.create(
            name="Sala de Espera",
            album="Exposição Popular",
            year=2024,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Exposic%CC%A7a%CC%83o%20Popular/Guerrinha%20-%20Exposic%CC%A7a%CC%83o%20Popular%20-%2006%20Sala%20de%20Espera.mp3",
            album_url="https://www.gpgc.info/releases/exposicao-popular",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Exposic%CC%A7a%CC%83o%20Popular/cover.png"
        )

        Track.objects.create(
            name="Madrugadas",
            album="Exposição Popular",
            year=2024,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Exposic%CC%A7a%CC%83o%20Popular/Guerrinha%20-%20Exposic%CC%A7a%CC%83o%20Popular%20-%2007%20Madrugadas.mp3",
            album_url="https://www.gpgc.info/releases/exposicao-popular",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Exposic%CC%A7a%CC%83o%20Popular/cover.png"
        )

        Track.objects.create(
            name="Fantasmas do Destino",
            album="Exposição Popular",
            year=2024,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Exposic%CC%A7a%CC%83o%20Popular/Guerrinha%20-%20Exposic%CC%A7a%CC%83o%20Popular%20-%2008%20Fantasmas%20do%20Destino.mp3",
            album_url="https://www.gpgc.info/releases/exposicao-popular",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Exposic%CC%A7a%CC%83o%20Popular/cover.png"
        )

        Track.objects.create(
            name="Quem Quer",
            album="Prédio Avenida Central",
            year=2024,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Pre%CC%81dio%20Avenida%20Central/Guerrinha%20-%20Pre%CC%81dio%20Avenida%20Central%20-%2001%20Quem%20Quer.mp3",
            album_url="https://www.gpgc.info/releases/predio-avenida-central",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Pre%CC%81dio%20Avenida%20Central/cover.jpg"
        )

        Track.objects.create(
            name="Classificações Geraes",
            album="Prédio Avenida Central",
            year=2024,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Pre%CC%81dio%20Avenida%20Central/Guerrinha%20-%20Pre%CC%81dio%20Avenida%20Central%20-%2002%20Classificac%CC%A7o%CC%83es%20Geraes.mp3",
            album_url="https://www.gpgc.info/releases/predio-avenida-central",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Pre%CC%81dio%20Avenida%20Central/cover.jpg"
        )

        Track.objects.create(
            name="Transito Invernal",
            album="Prédio Avenida Central",
            year=2024,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Pre%CC%81dio%20Avenida%20Central/Guerrinha%20-%20Pre%CC%81dio%20Avenida%20Central%20-%2003%20Transito%20Invernal.mp3",
            album_url="https://www.gpgc.info/releases/predio-avenida-central",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Pre%CC%81dio%20Avenida%20Central/cover.jpg"
        )

        Track.objects.create(
            name="O Encomendador",
            album="Prédio Avenida Central",
            year=2024,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Pre%CC%81dio%20Avenida%20Central/Guerrinha%20-%20Pre%CC%81dio%20Avenida%20Central%20-%2004%20O%20Encomendador.mp3",
            album_url="https://www.gpgc.info/releases/predio-avenida-central",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Pre%CC%81dio%20Avenida%20Central/cover.jpg"
        )

        Track.objects.create(
            name="Suspenso Pelo Ciclo Implícito",
            album="Suspenso Pelo Ciclo Implícito",
            year=2024,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Suspenso%20Pelo%20Ciclo%20Impli%CC%81cito/Guerrinha%20-%20Suspenso%20Pelo%20Ciclo%20Impli%CC%81cito%20-%2001%20Suspenso%20Pelo%20Ciclo%20Impli%CC%81cito.mp3",
            album_url="https://www.gpgc.info/releases/suspenso-pelo-ciclo-implicito",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/Suspenso%20Pelo%20Ciclo%20Impli%CC%81cito/cover.jpg"
        )

        Track.objects.create(
            name="A Fanfiqueira",
            album="A Fanfiqueira / O Fofoqueiro",
            year=2025,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/A%20Fanfiqueira%20%3A%20O%20Fofoqueiro/Guerrinha%20-%20A%20Fanfiqueira%20-%20O%20Fofoqueiro%20-%2001%20A%20Fanfiqueira.mp3",
            album_url="https://www.gpgc.info/releases/a-fanfiqueira-o-fofoqueiro",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/A%20Fanfiqueira%20%3A%20O%20Fofoqueiro/cover.jpg"
        )

        Track.objects.create(
            name="O Fofoqueiro",
            album="A Fanfiqueira / O Fofoqueiro",
            year=2025,
            song_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/A%20Fanfiqueira%20%3A%20O%20Fofoqueiro/Guerrinha%20-%20A%20Fanfiqueira%20-%20O%20Fofoqueiro%20-%2002%20O%20Fofoqueiro.mp3",
            album_url="https://www.gpgc.info/releases/a-fanfiqueira-o-fofoqueiro",
            cover_url="https://storage.googleapis.com/gpgc-api-bucket/RELEASED/GUERRINHA/A%20Fanfiqueira%20%3A%20O%20Fofoqueiro/cover.jpg"
        )

        self.stdout.write(self.style.SUCCESS("✅ Database seeded with tracks"))
