from rest_framework.generics import RetrieveUpdateAPIView

from .serializers import NotificationSerializer
from apps.notifications.models import Notification


class NotificationView(RetrieveUpdateAPIView):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()