from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static

from pavel_kinal import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.index),
    url(r'^((?P<lang_code>[a-z]+)/)?music/$', views.music, name="music"),
    url(r'^((?P<lang_code>[a-z]+)/)?video/$', views.video, name="video"),
    url(r'^((?P<lang_code>[a-z]+)/)?gear/$', views.gear, name="gear"),
    url(r'^((?P<lang_code>[a-z]+)/)?tab/$', views.tab, name="tab"),
    url(r'^bio/$', views.empty, name="bio"),
    url(r'^photo/$', views.empty, name="photo"),
    url(r'^merch/$', views.empty, name="merch"),
    url(r'^tuning/$', views.empty, name="tuning"),
    url(r'^contact/$', views.empty, name="contact"),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]


if settings.DEBUG:
    urlpatterns += [
        url(r'^layout/(?P<template>[A-z0-9_\-.]+)/$', views.layout),
    ]

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
