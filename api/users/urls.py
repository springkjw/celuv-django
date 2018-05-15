from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import (
    UserSocialLoginView, UserLoginView, UserModelViewSet,
    UserInfoView, UserImageView,
)

router = DefaultRouter()
router.register(r'', UserModelViewSet)

app_name = 'user'
urlpatterns = [
    path('info/', UserInfoView.as_view(), name='info'),
    path('image', UserImageView.as_view(), name='image'),
    path('social', UserSocialLoginView.as_view(), name='social'),
    path('login', UserLoginView.as_view(), name='login'),
    path('', include(router.urls)),
]
