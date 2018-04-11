from django.urls import path

from .views import ScheduleListAPIView

app_name = 'schedule'
urlpatterns = [
    path('', ScheduleListAPIView.as_view(), name='list'),
]