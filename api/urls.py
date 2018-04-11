from django.urls import path, include

app_name = 'api'
urlpatterns = [
    path('users/', include('api.users.urls', namespace='user')),
    path('schedules/', include('api.schedules.urls', namespace='schedule')),
    path('devices/', include('api.devices.urls', namespace='device')),
]
