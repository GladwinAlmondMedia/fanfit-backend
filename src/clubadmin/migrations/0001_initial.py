# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-15 17:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('competitions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_cycling_activity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_cycling_activity', to='competitions.Activity')),
                ('current_running_activity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_running_activity', to='competitions.Activity')),
                ('current_walking_activity', models.ForeignKey(blank=True, help_text='Enter the current walking activiy for competition', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='current_walking_activity', to='competitions.Activity')),
                ('football_club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.FootballClub')),
                ('next_cycling_activity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_cycling_activity', to='competitions.Activity')),
                ('next_running_activity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_running_activity', to='competitions.Activity')),
                ('next_walking_activity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_walking_activity', to='competitions.Activity')),
            ],
        ),
    ]
