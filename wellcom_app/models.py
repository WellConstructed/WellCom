from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime, timedelta


class Well(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=11, decimal_places=7)
    longitude = models.DecimalField(max_digits=11, decimal_places=7)
    country = models.CharField(max_length=200)  # Maybe automatically populate from lat/lon
    date_installed = models.DateField()
    depth_m = models.DecimalField(max_digits=5, decimal_places=1, null=True)
    last_update = models.DateTimeField()
    estimated_users = models.IntegerField()  # hidden
    cost_usd = models.DecimalField(max_digits=8, decimal_places=2)  # hidden
    contractor = models.CharField(max_length=200)  # hidden
    flow_rate_lpm = models.DecimalField(max_digits=6, decimal_places=2)  # hidden

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        self.last_update = timezone.now()
        return super(Well, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Note(models.Model):
    well = models.ForeignKey(Well)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class DeviceData(models.Model):
    well = models.ForeignKey(Well)
    timestamp = models.DateTimeField()
    temperature_c = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "{} | {} | {}".format(self.well, self.timestamp,
                                     self.temperature_c)


class Usage(models.Model):
    # TODO: Write functions to generate instances of this model from a list of DeviceData objects
    well = models.ForeignKey(Well)
    timestamp = models.DateTimeField()


class WaterTest(models.Model):
    """All parameters are recorded in mg/l unless otherwise stated"""

    well = models.ForeignKey(Well)
    date = models.DateField()
    pH = models.DecimalField(max_digits=15, decimal_places=2)
    turbidity_ntu = models.DecimalField(max_digits=15, decimal_places=2)
    app_true_colour_hz = models.IntegerField()
    conductivity_uscm = models.DecimalField(max_digits=15, decimal_places=2)
    temperature_c = models.DecimalField(max_digits=5, decimal_places=2)
    total_iron = models.DecimalField(max_digits=15, decimal_places=2)
    calcium = models.DecimalField(max_digits=15, decimal_places=2)
    magnesium = models.DecimalField(max_digits=15, decimal_places=2)
    chloride = models.DecimalField(max_digits=15, decimal_places=2)
    sulphate = models.DecimalField(max_digits=15, decimal_places=2)
    suspended_solids = models.DecimalField(max_digits=15, decimal_places=2)
    total_dissolved_solids = models.DecimalField(max_digits=15,
                                                 decimal_places=2)
    total_solids = models.DecimalField(max_digits=15, decimal_places=2)
    total_alkalinity = models.DecimalField(max_digits=15, decimal_places=2)
    total_hardness = models.DecimalField(max_digits=15, decimal_places=2)
    calcium_hardness = models.DecimalField(max_digits=15, decimal_places=2)
    magnesium_hardness = models.DecimalField(max_digits=15, decimal_places=2)
    copper = models.DecimalField(max_digits=15, decimal_places=2)
    nitrite_nitrogen = models.DecimalField(max_digits=15, decimal_places=2)
    nitrate_nitrogen = models.DecimalField(max_digits=15, decimal_places=2)
    fluoride = models.DecimalField(max_digits=15, decimal_places=2)
    mpn_index_tc_per_deciliter = models.DecimalField(max_digits=15,
                                                     decimal_places=2)
    ammonia_nitrogen = models.DecimalField(max_digits=15, decimal_places=2)
    manganese = models.DecimalField(max_digits=15, decimal_places=2)
    aluminum = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return 'Well {} tested on {}'.format(self.well, self.date)


class Test(models.Model):
    text = models.TextField(null=True)
    timestamp = models.DateTimeField()


class DeviceOutput(models.Model):
    well = models.ForeignKey(Well)
    batt_voltage_mv = models.IntegerField(default=-1)
    batt_percent_charged = models.IntegerField(default=-1)
    adc_voltage_mv = models.IntegerField(default=-1)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    # If Arduino NTP Time sync fails, upload_time and reading_interval_s
    # provide a method to approximate timestamps
    upload_time = models.DateTimeField(auto_now_add=True)
    reading_interval_s = models.IntegerField()
    temp_readings_c = models.TextField()


@receiver(post_save, sender=DeviceOutput)
def create_device_data(sender, instance, **kwargs):
    if (instance.start_time and instance.end_time):
        temp_readings = instance.temp_readings_c.split('|')
        time_ints = len(temp_readings) - 1
        time_passed = instance.end_time - instance.start_time
        print("Num Readings: ", len(temp_readings))
        print("Time intervals: ", time_ints)
        print("Time passed: ", time_passed)
        print("Time passed type: ", type(time_passed))
        print("Start time type: ", type(instance.start_time))

        for i in range(len(temp_readings)):

            print('reading ', i, temp_readings[i])
            ts = instance.start_time + (time_passed * i)
            reading = float(temp_readings[i])
            device_data = DeviceData(well=instance.well, timestamp=ts,
                                     temperature_c=reading)
            device_data.save()
    else:
        print('Did not collect both start and end times from Arduino')
        # write function to create data based on


class HourlyUsage(models.Model):
    well = models.ForeignKey(Well)
    timestamp = models.DateTimeField()
    usage_count = models.IntegerField()


class DailyUsage(models.Model):
    well = models.ForeignKey(Well)
    timestamp = models.DateTimeField()
    usage_count = models.IntegerField()


class WeeklyUsage(models.Model):
    well = models.ForeignKey(Well)
    timestamp = models.DateTimeField()
    usage_count = models.IntegerField()


class MonthlyUsage(models.Model):
    well = models.ForeignKey(Well)
    timestamp = models.DateTimeField()
    usage_count = models.IntegerField()


class YearlyUsage(models.Model):
    well = models.ForeignKey(Well)
    timestamp = models.DateTimeField()
    usage_count = models.IntegerField()
