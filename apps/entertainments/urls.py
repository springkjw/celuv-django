from django.urls import path

from .views import (
    EntertainmentListView,
    EntertainmentCreateAPIView,
    EntertainmentAPIView,
)

app_name = 'entertainment'
urlpatterns = [
    path('<int:pk>', EntertainmentAPIView.as_view(), name='api'),
    path('list', EntertainmentListView.as_view(), name='list'),
    path('create', EntertainmentCreateAPIView.as_view(), name='create'),
]
