from django.urls import path

from .views import ScheduleMonthlyView, ScheduleCreateView

app_name = 'schedule'
urlpatterns = [
    path('month', ScheduleMonthlyView.as_view(), name='month'),
    path('create', ScheduleCreateView.as_view(), name='create'),
]
