from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static

from pavel_kinal import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.index),
    url(r'^music/$', views.music, name="music"),
    url(r'^video/$', views.video, name="video"),
    url(r'^gear/$', views.empty, name="gear"),
    url(r'^tab/$', views.empty, name="tab"),
    url(r'^bio/$', views.empty, name="bio"),
    url(r'^photo/$', views.empty, name="photo"),
    url(r'^merch/$', views.empty, name="merch"),
    url(r'^tuning/$', views.empty, name="tuning"),
    url(r'^contact/$', views.empty, name="contact"),
]


if settings.DEBUG:
    urlpatterns += [
        url(r'^layout/(?P<template>[A-z0-9_\-.]+)/$', views.layout),
    ]

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
