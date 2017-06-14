# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-14 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
                ('description', models.TextField()),
                ('url', models.URLField(verbose_name='Video url')),
            ],
        ),
    ]
