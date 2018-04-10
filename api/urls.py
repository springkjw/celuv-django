from django.urls import path, include

app_name = 'api'
urlpatterns = [
    path('devices/', include('api.devices.urls', namespace='device')),
]
