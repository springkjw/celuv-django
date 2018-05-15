from django.urls import path, include

app_name = 'api'
urlpatterns = [
    path('users/', include('api.users.urls', namespace='user')),
    path('schedules/', include('api.schedules.urls', namespace='schedule')),
    path('celebrities/', include('api.celebritys.urls', namespace='celebrity')),
    path('devices/', include('api.devices.urls', namespace='device')),
    path('feedbacks/', include('api.feedbacks.urls', namespace='feedback')),
    path('notifications/', include('api.notifications.urls', namespace='notification')),
]
