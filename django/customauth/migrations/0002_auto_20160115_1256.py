# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-15 11:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customauth', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='token',
            new_name='tok',
        ),
    ]