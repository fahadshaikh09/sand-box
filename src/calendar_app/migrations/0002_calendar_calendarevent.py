# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-13 15:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calendar_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calendar_id_g', models.CharField(max_length=64)),
                ('summary', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=500)),
                ('time_zone', models.CharField(max_length=100)),
                ('eventSyncToken', models.CharField(max_length=64)),
                ('updated', models.DateTimeField()),
                ('lastSync', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CalendarEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id_g', models.CharField(max_length=64)),
                ('status', models.CharField(max_length=50)),
                ('htmlLink', models.URLField()),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('summary', models.CharField(max_length=500)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('transparency', models.BooleanField(default=False)),
                ('calendar_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendar_app.Calendar')),
            ],
        ),
    ]
