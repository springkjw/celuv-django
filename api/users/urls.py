from django.urls import path

from .views import (
    UserSocialLoginView,
)

app_name = 'user'
urlpatterns = [
    path('social', UserSocialLoginView.as_view(), name='social'),
]
