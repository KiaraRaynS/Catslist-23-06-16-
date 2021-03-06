# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 18:16
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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('preferredcity', models.CharField(choices=[('greenville', 'Greenville'), ('charleston', 'Charleston'), ('ashville', 'Asheville'), ('atlanta', 'Atlanta')], max_length=30, null=True)),
                ('profile photo', models.ImageField(blank=True, null=True, upload_to='profile_photos')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
