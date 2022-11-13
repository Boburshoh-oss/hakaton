from .models import SoilDevice, WaterDevice, Area, Region
from rest_framework import generics, viewsets, permissions
from .serializers import SoilDeviceSerializer, WaterDeviceSerializer, AreaSerializer, RegionSerializer
# Create your views here.
class SoilDeviceViewSet(generics.ListCreateAPIView):
    queryset = SoilDevice.objects.all()
    serializer_class = SoilDeviceSerializer
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return super().perform_create(serializer)

class SoilDeviceRetrieveViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = SoilDevice.objects.all()
    serializer_class = SoilDeviceSerializer

class WaterDeviceViewSet(generics.ListCreateAPIView):
    queryset = WaterDevice.objects.all()
    serializer_class = WaterDeviceSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        return super().perform_create(serializer)

class WaterDeviceRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WaterDevice.objects.all()
    serializer_class = WaterDeviceSerializer

class AreaViewSet(generics.ListCreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class AreaRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class RegionViewSet(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class RegionRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class MySoilDeviceViewSet(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = SoilDevice.objects.all()
    serializer_class = SoilDeviceSerializer

    def get_queryset(self):
        my_device = SoilDevice.objects.filter(owner=self.request.user)
        return my_device

class MyWaterDeviceViewSet(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = WaterDevice.objects.all()
    serializer_class = WaterDeviceSerializer

    def get_queryset(self):
        my_device = WaterDevice.objects.filter(owner=self.request.user)
        return my_device