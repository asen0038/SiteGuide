from django.db import models


class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    passenger_capacity = models.IntegerField(default=0)
    mass_kg = models.IntegerField(default=0)
