from django.urls import path
from measurements.views import calculate_distance_view

app_name = 'measurements'

urlpatterns = [
    path('', calculate_distance_view, name='calculate-view'),
]