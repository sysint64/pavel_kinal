from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from datetime import datetime


class TabAlbum(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    cover = ThumbnailerImageField()
    datetime = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


class TabTrack(models.Model):
    class Meta:
        default_related_name = "tracks"

    name = models.CharField(max_length=255)
    price = models.FloatField()
    album = models.ForeignKey(TabAlbum)

    def __str__(self):
        return self.name
