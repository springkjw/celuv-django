from django.urls import path

from .views import FeedbackAPIView

app_name = 'feedback'
urlpatterns = [
    path('feedback', FeedbackAPIView.as_view()),
]
