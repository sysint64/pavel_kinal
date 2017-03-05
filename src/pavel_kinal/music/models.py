from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField


class Album(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    cover = ThumbnailerImageField()


class Track(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    album = models.ForeignKey(Album)
