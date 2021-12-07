from django.db import models
from django.utils import timezone


class Ripening_chamber_zone(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.name


class Controler_type(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Controler(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    type = models.ForeignKey(Controler_type, on_delete=models.CASCADE)
    chamber_zone = models.ForeignKey(Ripening_chamber_zone, on_delete=models.CASCADE)
    chart_url = models.URLField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.chart_url = f"localhost:8000/devices/{self.id}"
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name


CONTROLER_RECORD_CHOICES = [('True', True), ('False', False),]
class Controler_record(models.Model):
    status = models.CharField(max_length=5, choices=CONTROLER_RECORD_CHOICES, default=0, blank=False)
    datetime = models.DateTimeField(default=timezone.now)
    controler = models.ForeignKey(Controler, on_delete=models.CASCADE, default=None)


class Sensor_type(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Sensor(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    units = models.TextField(max_length=200, blank=True)
    type = models.ForeignKey(Sensor_type, on_delete=models.CASCADE)
    chamber_zone = models.ForeignKey(Ripening_chamber_zone, on_delete=models.CASCADE)
    chart_url = models.URLField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.chart_url = f"localhost:8000/sensors/{self.id}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Sensor_measure(models.Model):
    measure = models.IntegerField()
    datetime = models.DateTimeField(default=timezone.now)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)