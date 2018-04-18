from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import (
    UserSocialLoginView, UserLoginView, UserModelViewSet,
)

router = DefaultRouter()
router.register(r'', UserModelViewSet)

app_name = 'user'
urlpatterns = [
    path('', include(router.urls)),
    path('social', UserSocialLoginView.as_view(), name='social'),
    path('login', UserLoginView.as_view(), name='login'),
]
