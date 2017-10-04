# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-15 14:34
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('country_code', models.CharField(max_length=4, primary_key=True, serialize=False, verbose_name='Код страны')),
                ('country_name', models.CharField(default='', max_length=255, verbose_name='Название')),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Язык',
                'verbose_name_plural': 'Языки',
            },
        ),
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vk_url', models.URLField(verbose_name='VK')),
                ('fb_url', models.URLField(verbose_name='Facebook')),
                ('tw_url', models.URLField(verbose_name='Twitter')),
            ],
        ),
        migrations.CreateModel(
            name='PreferencesTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', ckeditor_uploader.fields.RichTextUploadingField()),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='preferences.Language', verbose_name='Язык')),
                ('preferences', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='preferences.Preferences')),
            ],
        ),
        migrations.AddField(
            model_name='language',
            name='languages',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='preferences.Languages'),
        ),
    ]