import datetime
from rest_framework import serializers

from apps.schedules.models import Schedule
from api.celebritys.serializers import CelebritySerializer


class ScheduleSerializer(serializers.ModelSerializer):
    # 스케줄 직렬화
    start = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()
    celeb = CelebritySerializer(many=True, read_only=True, source='celebrity')
    schedule_type = serializers.SerializerMethodField()
    is_notification = serializers.SerializerMethodField()

    class Meta:
        model = Schedule
        fields = (
            'id',
            'start',
            'content',
            'celeb',
            'schedule_type',
            'is_notification',
        )

    def get_start(self, obj):
        return datetime.datetime.strftime(obj.schedule, '%Y-%m-%d %H:%m')

    def get_content(self, obj):
        return obj.title

    def get_schedule_type(self, obj):
        schedule_type = obj.schedulecategory_set.all()
        if not schedule_type.exists():
            return None
        return schedule_type.first().first_category

    def get_is_notification(self, obj):
        return False