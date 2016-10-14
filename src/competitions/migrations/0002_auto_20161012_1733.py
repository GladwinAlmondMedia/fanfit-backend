# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-12 17:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='competitors',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='category',
        ),
        migrations.AddField(
            model_name='activity',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='competitions.ActivityCategory'),
            preserve_default=False,
        ),
    ]
