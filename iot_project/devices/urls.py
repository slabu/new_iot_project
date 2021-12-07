from django.urls import path
from .views import chart, DeviceChartView, DeviceListView, SensorChartView

urlpatterns = [
    path('devices/', DeviceListView.as_view(), name='devices'),
    path('devices/<int:pk>/', DeviceChartView.as_view(), name='device-chart'),
    path('sensors/<int:pk>/', SensorChartView.as_view(), name='sensor-chart'),
]