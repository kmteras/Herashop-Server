# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-22 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Herashop', '0002_auto_20170122_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='lat',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='store',
            name='lon',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
