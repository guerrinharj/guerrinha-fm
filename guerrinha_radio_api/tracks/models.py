from django.db import models

# Create your models here.
class Track(models.Model):
    name = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    year = models.IntegerField()
    song_url = models.URLField()
    album_url = models.URLField()
    cover_url = models.URLField()