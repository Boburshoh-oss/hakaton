from django.contrib import admin
from .models import SoilDevice, WaterDevice, Area,Region
# Register your models here.
admin.site.register(SoilDevice)
admin.site.register(WaterDevice)
admin.site.register(Area)
admin.site.register(Region)