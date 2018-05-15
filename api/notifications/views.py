from rest_framework import mixins
from rest_framework.generics import RetrieveUpdateAPIView, GenericAPIView
from rest_framework.response import Response

from apps.notifications.models import Notification

from .serializers import NotificationSerializer, NotificationCelebritySerializer


class NotificationAPIView(RetrieveUpdateAPIView):
    serializer_class = NotificationSerializer

    def get_object(self):
        obj, _ = Notification.objects.get_or_create(
            user=self.request.user,
            notification_type='c'
        )
        return obj

    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class NotificationCelebrityAPIView(GenericAPIView):
    serializer_class = NotificationCelebritySerializer

    def get_object(self):
        obj, _ = Notification.objects.get_or_create(
            user=self.request.user,
            notification_type='c'
        )
        return obj

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = self.get_object()
        is_active = serializer.data.get('is_active')
        if is_active:
            instance.target.append(kwargs.get('celebrity_id'))
        else:
            instance.target.remove(kwargs.get('celebrity_id'))
        instance.save()
        return Response()
