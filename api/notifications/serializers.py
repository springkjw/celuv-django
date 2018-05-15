from rest_framework import serializers

from apps.notifications.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    notification = serializers.SerializerMethodField()
    event = serializers.SerializerMethodField()
    
    class Meta:
        model = Notification
        fields = [
            'notification',
            'event',
        ]

    def get_notification(self, obj):
        return True

    def get_event(self, obj):
        return True