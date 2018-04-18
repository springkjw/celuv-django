from django.urls import path

from .views import ScheduleMonthlyView, ScheduleCreateView, ScheduleDetailView, ScheduleDeleteView

app_name = 'schedule'
urlpatterns = [
    path('month', ScheduleMonthlyView.as_view(), name='month'),
    path('create', ScheduleCreateView.as_view(), name='create'),
    path('<int:pk>', ScheduleDetailView.as_view(), name='detail'),
    path('<int:pk>/delete', ScheduleDeleteView.as_view(), name='delete'),
]
