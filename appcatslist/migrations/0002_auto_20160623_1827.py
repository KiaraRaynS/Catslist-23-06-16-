# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcatslist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='preferredcity',
            field=models.CharField(blank=True, choices=[('greenville', 'Greenville'), ('charleston', 'Charleston'), ('ashville', 'Asheville'), ('atlanta', 'Atlanta')], max_length=30, null=True),
        ),
    ]
