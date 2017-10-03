from django.contrib import admin

from pavel_kinal.gear.models import Gear

admin.site.register(Gear, admin.ModelAdmin)
