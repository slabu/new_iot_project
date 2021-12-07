from django.contrib import admin

from devices.models import Ripening_chamber_zone, Controler_type, Controler, Controler_record, Sensor_type, Sensor, \
    Sensor_measure


class ControlerAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'chamber_zone', 'chart_url')

    list_filter = ('type', 'chamber_zone',)


class ControlerTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ControlerRecordAdmin(admin.ModelAdmin):
    list_display = ('controler', 'status', 'datetime',)

    list_filter = ('status',)


class SensorAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'chamber_zone', 'chart_url')

    list_filter = ('type', 'chamber_zone',)


class SensorTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class SensorMeasureAdmin(admin.ModelAdmin):
    list_display = ('sensor', 'measure', 'datetime',)

    list_filter = ('sensor', 'measure',)


class RipeningChamberZoneAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Ripening_chamber_zone, RipeningChamberZoneAdmin)
admin.site.register(Controler_type, ControlerTypeAdmin)
admin.site.register(Controler, ControlerAdmin)
admin.site.register(Controler_record, ControlerRecordAdmin)
admin.site.register(Sensor_type, SensorTypeAdmin)
admin.site.register(Sensor, SensorAdmin)
admin.site.register(Sensor_measure, SensorMeasureAdmin)