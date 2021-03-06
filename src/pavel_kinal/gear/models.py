from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField


class Gear(models.Model):
    image = ThumbnailerImageField()
    name = models.TextField()

    def __str__(self):
        return self.name

