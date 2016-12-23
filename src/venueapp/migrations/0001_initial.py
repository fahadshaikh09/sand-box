# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-23 16:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venueName', models.CharField(max_length=500)),
                ('summary', models.CharField(max_length=1000)),
                ('website', models.URLField(blank=True)),
                ('socialLink', models.URLField(blank=True)),
                ('coverPhoto', models.ImageField(blank=True, upload_to=b'')),
                ('logo', models.ImageField(blank=True, upload_to=b'')),
                ('contactInfo', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=15)),
                ('confirmation', models.BooleanField(default=False)),
                ('wifiAvailability', models.BooleanField(default=False)),
                ('capacity', models.IntegerField(default=0)),
                ('cateringAvailability', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_venue', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
