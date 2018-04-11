from django.urls import path

from .views import HomeView, PrivateView

app_name = 'base'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('private', PrivateView.as_view(), name='private'),
]
