# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-16 04:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(default=datetime.datetime(2017, 2, 16, 4, 33, 23, 705354, tzinfo=utc)),
        ),
    ]
