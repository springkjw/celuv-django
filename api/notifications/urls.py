from django.urls import path

from . import views

app_name = 'notification'
urlpatterns = [
    path('notification', views.NotificationView.as_view(), name='notification'),
]