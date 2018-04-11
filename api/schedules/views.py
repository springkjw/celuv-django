from rest_framework.generics import ListAPIView

from apps.schedules.models import Schedule

from .serializers import ScheduleSerializer


class ScheduleListAPIView(ListAPIView):
    # 스케줄 목록 API
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    