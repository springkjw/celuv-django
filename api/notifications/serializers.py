from rest_framework import serializers

from apps.notifications.models import Notification
from apps.celebritys.models import Celebrity


class NotificationSerializer(serializers.ModelSerializer):
    notification = serializers.SerializerMethodField()
    celebrity = serializers.SerializerMethodField()
    is_active = serializers.BooleanField(
        write_only=True,
    )

    class Meta:
        model = Notification
        fields = [
            'notification',
            'celebrity',
            'is_active',
        ]

    def get_notification(self, obj):
        if obj.user.celebrity_set.all().count() == len(obj.target):
            return True
        return False

    def get_celebrity(self, obj):
        celebrity = obj.user.celebrity_set.all()
        print(obj.target)
        data = [{
            'celebrity_id': c.id,
            'celebrity': c.name,
            'celebrity_image': c.get_profile_image,
            'is_active': str(c.id) in obj.target
        } for c in celebrity]
        return data

    def update(self, instance, validated_data):
        is_active = validated_data.get('is_active', False)
        if is_active:
            celebrity = instance.user.celebrity_set.all()
            instance.target = [str(c.id) for c in celebrity]
        else:
            instance.target = []
        instance.save()
        return instance


class NotificationCelebritySerializer(serializers.Serializer):
    is_active = serializers.BooleanField(

    )
