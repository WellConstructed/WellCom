from django.contrib import admin
from .models import (Well, Note, DeviceData, Usage, WaterTest, Test,
                     DeviceOutput)

# Register your models here.
admin.site.register(Well)
admin.site.register(Note)
admin.site.register(DeviceData)
admin.site.register(Usage)
admin.site.register(WaterTest)
admin.site.register(Test)
admin.site.register(DeviceOutput)
