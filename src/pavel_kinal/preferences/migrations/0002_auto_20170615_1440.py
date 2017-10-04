# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-15 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preferences',
            name='tw_url',
        ),
        migrations.AddField(
            model_name='preferences',
            name='instagram_url',
            field=models.URLField(blank=True, verbose_name='Instagram'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='soundcloud_url',
            field=models.URLField(blank=True, verbose_name='Soundcloud'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='twitch_url',
            field=models.URLField(blank=True, verbose_name='Twitch'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='twitter_url',
            field=models.URLField(blank=True, verbose_name='Twitter'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='youtube_url',
            field=models.URLField(blank=True, verbose_name='YouTube'),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='fb_url',
            field=models.URLField(blank=True, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='preferences',
            name='vk_url',
            field=models.URLField(blank=True, verbose_name='VK'),
        ),
    ]