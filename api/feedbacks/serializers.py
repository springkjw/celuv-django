from rest_framework import serializers

from apps.feedbacks.models import Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Feedback
        fields = [
            'user',
            'category',
            'content',
        ]
