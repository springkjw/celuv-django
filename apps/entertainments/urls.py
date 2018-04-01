from django.urls import path

from .views import (
    EntertainmentListView,
    EntertainmentCreateView,
)

app_name = 'entertainment'
urlpatterns = [
    path('list', EntertainmentListView.as_view(), name='list'),
    path('create', EntertainmentCreateView.as_view(), name='create'),
]
