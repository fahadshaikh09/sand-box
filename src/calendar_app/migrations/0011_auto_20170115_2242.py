# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-15 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendar_app', '0010_auto_20170114_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendarevent',
            name='created',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='calendarevent',
            name='htmlLink',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='calendarevent',
            name='updated',
            field=models.DateTimeField(blank=True),
        ),
    ]
