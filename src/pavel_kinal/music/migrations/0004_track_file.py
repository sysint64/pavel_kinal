# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-19 06:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_album_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='file',
            field=models.FileField(blank=True, upload_to='music/'),
        ),
    ]
