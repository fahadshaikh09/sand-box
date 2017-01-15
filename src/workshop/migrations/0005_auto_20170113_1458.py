# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-13 14:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0004_auto_20161226_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='enrolled_users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]