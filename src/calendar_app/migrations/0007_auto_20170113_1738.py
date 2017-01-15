# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-13 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_app', '0006_auto_20170113_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='eventSyncToken',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='location',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='summary',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='timeZone',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='updated',
            field=models.DateTimeField(blank=True),
        ),
    ]