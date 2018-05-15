from django.urls import path

from .views import FeedbackAPIView, ReportAPIView, ReportImageAPIView

app_name = 'feedback'
urlpatterns = [
    path('feedback', FeedbackAPIView.as_view()),
    path('report', ReportAPIView.as_view()),
    path('report/image', ReportImageAPIView.as_view()),
]
