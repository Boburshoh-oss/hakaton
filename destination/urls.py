from .views import (SoilDeviceViewSet, WaterDeviceViewSet, AreaViewSet,  
    RegionViewSet, MySoilDeviceViewSet, SoilDeviceRetrieveViewSet, WaterDeviceRetrieveView, AreaRetrieveView, RegionRetrieveView)
from django.urls import path




urlpatterns = [
    path('soil-device/', SoilDeviceViewSet.as_view()),
    path('soil-device/<int:pk>/', SoilDeviceRetrieveViewSet.as_view()),
    path('water-device/', WaterDeviceViewSet.as_view()),
    path('water-device/<int:pk>/', WaterDeviceRetrieveView.as_view()),
    path('area/', AreaViewSet.as_view()),
    path('area/<int:pk>/', AreaRetrieveView.as_view()),
    path('region/', RegionViewSet.as_view()),
    path('region/<int:pk>/', RegionRetrieveView.as_view()),
    path('my-soil-device/', MySoilDeviceViewSet.as_view()),
    path('my-water-device/', MySoilDeviceViewSet.as_view()),
]
