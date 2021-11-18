from django.contrib import admin

from products.models import Cheese, Cheese_condition, Cheese_batch
from devices.models import Ripening_chamber_zone, Controler_type, Controler, Controler_record, Sensor_type, Sensor, \
    Sensor_measure
# Register your models here.

admin.site.register(Cheese)
admin.site.register(Cheese_condition)
admin.site.register(Cheese_batch)
admin.site.register(Ripening_chamber_zone)
admin.site.register(Controler_type)
admin.site.register(Controler)
admin.site.register(Controler_record)
admin.site.register(Sensor_type)
admin.site.register(Sensor)
admin.site.register(Sensor_measure)