from django.urls import path

from .views import ReportListView, ReportConfirmUpdateView

app_name = 'feedback'
urlpatterns = [
    path('', ReportListView.as_view(), name='list'),
    path('<pk>/update', ReportConfirmUpdateView.as_view(), name='update'),
]