# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-22 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Herashop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]