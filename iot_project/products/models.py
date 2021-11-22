from django.db import models
from django.utils import timezone

from devices.models import Ripening_chamber_zone


class Cheese(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    ingredients = models.TextField(null=False)
    ripening_period = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Cheese_condition(models.Model):
    current_condition = models.TextField(max_length=300)
    previous_condition = models.CharField(max_length=30, null=False)
    term_days = models.IntegerField()
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)


class Cheese_batch(models.Model):
    amount = models.IntegerField()
    datetime = models.DateTimeField(default=timezone.now)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)
    chamber_zone = models.ForeignKey(Ripening_chamber_zone, on_delete=models.CASCADE)