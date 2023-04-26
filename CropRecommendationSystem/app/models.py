from django.db import models

# Create your models here.
from django.db import models


class Crop(models.Model):
    name = models.CharField(max_length=20)
    N = models.PositiveIntegerField(default=0)
    K = models.PositiveIntegerField(default=0)
    humidity = models.PositiveIntegerField(default=0)
    temperature = models.PositiveIntegerField(default=0)
    ph = models.PositiveIntegerField(default=0)
    rainfall = models.PositiveIntegerField(default=0)


class Location(models.Model):
    name = models.CharField(max_length=20)
    crop = models.ForeignKey(Crop,on_delete=models.CASCADE,related_name="crop_location")



