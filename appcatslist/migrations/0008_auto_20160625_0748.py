# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 07:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appcatslist', '0007_auto_20160624_2100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offerpost',
            name='category',
        ),
        migrations.AddField(
            model_name='subcategorylist',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appcatslist.CategoryList'),
            preserve_default=False,
        ),
    ]