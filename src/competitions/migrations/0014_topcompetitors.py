# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-23 19:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('competitions', '0013_remove_workout_new_bool'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopCompetitors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.Activity')),
                ('first', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_top_user', to=settings.AUTH_USER_MODEL)),
                ('second', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_top_user', to=settings.AUTH_USER_MODEL)),
                ('third', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='third_top_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]