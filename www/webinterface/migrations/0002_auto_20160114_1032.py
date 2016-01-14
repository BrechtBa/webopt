# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 09:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webinterface', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='daily_computation_time',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_call',
            field=models.DateTimeField(default=datetime.datetime(1970, 1, 1, 1, 0)),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='used_computation_time',
            field=models.IntegerField(default=0),
        ),
    ]
