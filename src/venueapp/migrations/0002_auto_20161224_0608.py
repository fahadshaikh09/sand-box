# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-24 06:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('venueapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profileapp.Member'),
        ),
    ]
