# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-16 18:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20160115_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='token',
            name='last_solution',
        ),
        migrations.RemoveField(
            model_name='token',
            name='last_supplied_problem',
        ),
    ]
