# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-23 18:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0012_workout_new_bool'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='new_bool',
        ),
    ]
