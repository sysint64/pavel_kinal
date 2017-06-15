# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-15 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0003_remove_preferencestranslation_bio'),
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='preferences.Language', verbose_name='Язык')),
            ],
            options={
                'default_related_name': 'translations',
            },
        ),
        migrations.RemoveField(
            model_name='video',
            name='description',
        ),
        migrations.AddField(
            model_name='videotranslation',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='video.Video'),
        ),
    ]
