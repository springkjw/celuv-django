from rest_framework import serializers

from apps.schedules.models import Schedule
from api.celebritys.serializers import CelebritySerializer


class ScheduleSerializer(serializers.ModelSerializer):
    # 스케줄 직렬화
    start = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()
    celeb = CelebritySerializer(many=True, read_only=True, source='celebrity')

    class Meta:
        model = Schedule
        fields = (
            'id',
            'start',
            'content',
            'celeb',
        )

    def get_start(self, obj):
        return obj.schedule

    def get_content(self, obj):
        return obj.title