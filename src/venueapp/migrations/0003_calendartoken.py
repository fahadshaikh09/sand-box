# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-24 06:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('venueapp', '0002_auto_20161224_0608'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.TextField()),
                ('refresh_token', models.TextField(blank=True)),
                ('token_expiry', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_venue', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
