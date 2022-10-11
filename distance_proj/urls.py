
from django.contrib import admin
from django.urls import path, include
from measurements.views import calculate_distance_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('measurements.urls', 'measurements'), namespace='measurements')),
]
