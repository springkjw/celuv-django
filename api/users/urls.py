from django.urls import path
from .views import (
    UserSocialLoginView, UserLoginView, UserModelViewSet,
    UserInfoView, UserImageView,
)

app_name = 'user'
urlpatterns = [
    path('info/', UserInfoView.as_view(), name='info'),
    path('image', UserImageView.as_view(), name='image'),
    path('social', UserSocialLoginView.as_view(), name='social'),
    path('login', UserLoginView.as_view(), name='login'),
    path('<str:uuid>/', UserModelViewSet.as_view({
        'get': 'retrieve'
    })),
]
