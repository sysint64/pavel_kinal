from django.contrib import admin

from pavel_kinal.music.models import Album, Track


class TrackInlineAdmin(admin.TabularInline):
    model = Track
    extra = 1
    max_num = 999


class AlbumAdmin(admin.ModelAdmin):
    inlines = [TrackInlineAdmin]


admin.site.register(Album, AlbumAdmin)
