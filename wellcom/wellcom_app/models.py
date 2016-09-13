from django.db import models
from django.utils import timezone


class Well(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=11, decimal_places=7)
    longitude = models.DecimalField(max_digits=11, decimal_places=7)
    country = models.CharField(max_length=200)  # Maybe automatically populate from lat/lon
    date_installed = models.DateField()
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
    date = models.DateField()
    usage_count = models.IntegerField()

    def __str__(self):
        return self.title


class WaterTest(models.Model):
    """All parameters are recorded in mg/l unless otherwise stated"""

    well = models.ForeignKey(Well)
    date = models.DateField()
    pH = models.DecimalField(max_digits=15, decimal_places=4)
    turbidity_ntu = models.DecimalField(max_digits=15, decimal_places=4)
    app_true_colour_hz = models.IntegerField()
    conductivity_uscm = models.DecimalField(max_digits=15, decimal_places=4)
    temperature_c = models.DecimalField(max_digits=5, decimal_places=2)
    total_iron = models.DecimalField(max_digits=15, decimal_places=4)
    calcium = models.DecimalField(max_digits=15, decimal_places=4)
    magnesium = models.DecimalField(max_digits=15, decimal_places=4)
    chloride = models.DecimalField(max_digits=15, decimal_places=4)
    sulphate = models.DecimalField(max_digits=15, decimal_places=4)
    suspended_solids = models.DecimalField(max_digits=15, decimal_places=4)
    total_dissolved_solids = models.DecimalField(max_digits=15, decimal_places=4)
    total_solids = models.DecimalField(max_digits=15, decimal_places=4)
    total_alkalinity = models.DecimalField(max_digits=15, decimal_places=4)
    total_hardness = models.DecimalField(max_digits=15, decimal_places=4)
    calcium_hardness = models.DecimalField(max_digits=15, decimal_places=4)
    magnesium_hardness = models.DecimalField(max_digits=15, decimal_places=4)
    copper = models.DecimalField(max_digits=15, decimal_places=4)
    nitrite_nitrogen = models.DecimalField(max_digits=15, decimal_places=4)
    nitrate_nitrogen = models.DecimalField(max_digits=15, decimal_places=4)
    fluoride = models.DecimalField(max_digits=15, decimal_places=4)
    mpn_index_tc_per_deciliter = models.DecimalField(max_digits=15, decimal_places=4)
    ammonia_nitrogen = models.DecimalField(max_digits=15, decimal_places=4)
    manganese = models.DecimalField(max_digits=15, decimal_places=4)
    aluminum = models.DecimalField(max_digits=15, decimal_places=4)

    def __str__(self):
        return 'Well {} tested on {}'.format(self.well, self.date)
