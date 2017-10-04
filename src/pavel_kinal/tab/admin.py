from django.contrib import admin

from pavel_kinal.tab.models import TabTrack, TabAlbum


class TabTrackInlineAdmin(admin.TabularInline):
    model = TabTrack
    extra = 1
    max_num = 999


class TabAlbumAdmin(admin.ModelAdmin):
    inlines = [TabTrackInlineAdmin]


admin.site.register(TabAlbum, TabAlbumAdmin)
