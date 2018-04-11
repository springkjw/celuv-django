from django.urls import path

from .views import (
    UserSocialLoginView, UserLoginView,
)

app_name = 'user'
urlpatterns = [
    path('social', UserSocialLoginView.as_view(), name='social'),
    path('login', UserLoginView.as_view(), name='login'),
]
