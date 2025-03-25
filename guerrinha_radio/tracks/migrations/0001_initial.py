# Generated by Django 5.1.7 on 2025-03-25 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('album', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('song_url', models.URLField()),
                ('album_url', models.URLField()),
                ('cover_url', models.URLField()),
            ],
        ),
    ]
