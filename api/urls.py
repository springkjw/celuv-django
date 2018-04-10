from django.urls import path, include

app_name = 'api'
urlpatterns = [
    path('users/', include('api.users.urls', namespace='user')),
    path('devices/', include('api.devices.urls', namespace='device')),
]
