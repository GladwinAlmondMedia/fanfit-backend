# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-15 20:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0009_auto_20161015_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workout_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
