from django.urls import path

from .views import (
    UserFanListView,
    UserFanAPIView,
    UserManagerListView, 
    UserManagerCreateAPIView,
)

app_name = 'user'
urlpatterns = [
    path('fan', UserFanListView.as_view(), name='fan'),
    path('fan/<int:pk>', UserFanAPIView.as_view(), name='fan_detail'),
    path('manager', UserManagerListView.as_view(), name='manager'),
    path('manager/create', UserManagerCreateAPIView.as_view(), name='manager_create'),
]