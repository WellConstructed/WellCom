# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 15:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wellcom_app', '0009_test_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deviceinput',
            name='temp_readings',
        ),
        migrations.RemoveField(
            model_name='deviceinput',
            name='time_added',
        ),
        migrations.RemoveField(
            model_name='deviceinput',
            name='time_int_seconds',
        ),
        migrations.AddField(
            model_name='deviceinput',
            name='adc_voltage_mv',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='deviceinput',
            name='batt_percent_charged',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='deviceinput',
            name='batt_voltage_mv',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='deviceinput',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deviceinput',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deviceinput',
            name='temp_readings_c',
            field=models.TextField(default='None'),
            preserve_default=False,
        ),
    ]
