from django.db import models
from django.conf import settings


class Region(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name

class Area(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey('destination.Region',on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    


class SoilDevice(models.Model):
    area = models.ForeignKey("destination.Area",on_delete=models.SET_NULL,null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    soil_moisture = models.IntegerField(blank=True,null=True)
    soil_temperature = models.IntegerField(blank=True,null=True)
    soil_microelement = models.IntegerField(blank=True,null=True)
    power_battery = models.IntegerField(blank=True,null=True)
    
    def __str__(self) -> str:
        return self.name

class WaterDevice(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)
    area = models.ForeignKey("destination.Area",on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    water_level = models.IntegerField(blank=True,null=True)
    water_temperature = models.IntegerField(blank=True,null=True)
    power_battery = models.IntegerField(blank=True,null=True)
    
    def __str__(self) -> str:
        return self.name


