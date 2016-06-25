# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 21:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appcatslist', '0006_auto_20160624_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategoryList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='offerpost',
            name='subcategory',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appcatslist.SubCategoryList'),
            preserve_default=False,
        ),
    ]
