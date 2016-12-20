# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-20 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0002_auto_20161220_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='cost',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='information',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='event',
            name='photo',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='event',
            name='terms',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='capacity',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='contactInfo',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='venue',
            name='coverPhoto',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='venue',
            name='gmailCalender',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='venue',
            name='logo',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='venue',
            name='socialLink',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='venue',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]