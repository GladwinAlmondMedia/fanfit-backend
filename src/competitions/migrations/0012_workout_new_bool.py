# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-23 18:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0011_auto_20161017_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='new_bool',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
