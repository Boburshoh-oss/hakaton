from rest_framework import serializers
from .models import SoilDevice,WaterDevice,Area,Region

class SoilDeviceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SoilDevice
        fields = "__all__"

class WaterDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterDevice
        fields = "__all__"
        
        
class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = "__all__"

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"