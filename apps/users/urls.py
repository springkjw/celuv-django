from django.urls import path

from .views import (
    UserFanListView,
    UserFanAPIView,
    UserManagerListView,
    UserManagerCreateView,
    UserLoginView,
    UserLogoutView,
)

app_name = 'user'
urlpatterns = [
    path('login', UserLoginView.as_view(), name='login'),
    path('logout', UserLogoutView.as_view(), name='logout'),
    path('fan', UserFanListView.as_view(), name='fan'),
    path('fan/<int:pk>', UserFanAPIView.as_view(), name='fan_detail'),
    path('manager', UserManagerListView.as_view(), name='manager'),
    path('manager/create', UserManagerCreateView.as_view(), name='manager_create'),
]
