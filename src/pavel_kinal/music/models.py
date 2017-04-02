from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from datetime import datetime


class Album(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    cover = ThumbnailerImageField()
    datetime = models.DateTimeField(default=datetime.now)


class Track(models.Model):
    class Meta:
        default_related_name = "tracks"

    name = models.CharField(max_length=255)
    price = models.FloatField()
    album = models.ForeignKey(Album)
    file = models.FileField(upload_to="music/", blank=True)
    duration = models.CharField(max_length=4, default="0:00")
