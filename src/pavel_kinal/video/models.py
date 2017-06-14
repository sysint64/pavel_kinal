from django.conf import settings
from django.db import models


class Video(models.Model):
    name = models.CharField(verbose_name="Name", max_length=60)
    description = models.TextField()
    url = models.URLField(verbose_name="Video url")

    def __str__(self):
        return self.name

    @property
    def video_id(self):
        try:
            return self.url.split("?v=")[1]
        except IndexError:
            return None

    @property
    def thumbnail(self):
        if self.video_id is None:
            return settings.STATIC_URL + "images/not_found.jpg"

        return "https://img.youtube.com/vi/%s/hqdefault.jpg" % self.video_id

    @property
    def embedded_video_url(self):
        if self.video_id is None:
            return None

        return "https://www.youtube.com/embed/%s" % self.video_id
