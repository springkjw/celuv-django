from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import NotificationSerializer
from apps.notifications.models import Notification


class NotificationView(GenericAPIView):
    serializer_class = NotificationSerializer

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        return Response(serializer.data)
