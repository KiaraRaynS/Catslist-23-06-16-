# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcatslist', '0004_auto_20160623_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='username',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='userdescription',
            field=models.TextField(blank=True, null=True),
        ),
    ]
