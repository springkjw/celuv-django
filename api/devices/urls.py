from django.urls import path, include

from push_notifications.api.rest_framework import APNSDeviceAuthorizedViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('apns', APNSDeviceAuthorizedViewSet)

app_name = 'device'
urlpatterns = [
    path('', include(router.urls)),
]
