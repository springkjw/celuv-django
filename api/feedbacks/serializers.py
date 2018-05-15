from rest_framework import serializers

from apps.feedbacks.models import Feedback, Report, ReportImage


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


class ReportSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    celeb = serializers.SerializerMethodField()

    class Meta:
        model = Report
        fields = [
            'id',
            'user',
            'celeb',
            'url',
        ]

    def get_celeb(self, obj):
        return obj.celebrity


class ReportImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportImage
        fields = [
            'report',
            'image_url',
        ]
