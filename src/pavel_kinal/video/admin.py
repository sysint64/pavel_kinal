from django.contrib import admin

from pavel_kinal.preferences.admin import LanguageListDisplayMixin, SingleLanguageInline
from pavel_kinal.video.models import Video, VideoTranslation


class VideoTranslationInline(SingleLanguageInline):
    model = VideoTranslation
    extra = 0
    max_num = 999


class VideoAdmin(LanguageListDisplayMixin, admin.ModelAdmin):
    inlines = [VideoTranslationInline]
    list_display = "__str__", "languages"


admin.site.register(Video, VideoAdmin)
