# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 14:16
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import random


def add_hourly_usage(apps, schema_editor):
    hours_daily = {0: (0,5), 1: (0,5), 2: (0,5), 3: (0,5), 4: (0,5), 5: (5,10), 6: (5,10), 7: (5,10), 8: (5,10),
                   9: (10,30), 10: (10,30), 11: (30,50), 12: (30,50), 13: (30,50), 14: (10,30), 15: (10,30), 16: (10,30),
                   17: (25,45), 18: (25,45), 19: (10,30), 20: (10,30), 21: (5,10), 22: (0,5), 23: (0,5)}

    wells = [{"id": 1, "pop": .5},
             {"id": 2, "pop": .6},
             {"id": 3, "pop": .4},
             {"id": 4, "pop": .55},
             {"id": 5, "pop": .15},
             {"id": 6, "pop": .8},
             {"id": 7, "pop": 0}]

    HourlyUsage = apps.get_model("wellcom_app", "HourlyUsage")

    for well in wells:
        cur = datetime.datetime(2016, 9, 30, 0, 0)
        for index in range(24):
            cur -= datetime.timedelta(hours=1)
            pump_count = random.choice(range(*hours_daily[cur.hour]))
            cur = datetime.datetime(cur.year, cur.month, cur.day, cur.hour)
            hourly_usage = HourlyUsage(well_id=well["id"],
                                       timestamp=cur.isoformat(),
                                       usage_count=pump_count * well["pop"])
            hourly_usage.save()


class Migration(migrations.Migration):

    dependencies = [
        ('wellcom_app', '0016_dailyusage_hourlyusage_monthlyusage_weeklyusage_yearlyusage'),
    ]

    operations = [
        migrations.RunPython(add_hourly_usage)
    ]
