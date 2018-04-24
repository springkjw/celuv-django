from datetime import date, datetime, timedelta
from rest_framework.generics import ListAPIView

from apps.schedules.models import Schedule
from apps.celebritys.models import Celebrity

from .serializers import ScheduleSerializer


class ScheduleListAPIView(ListAPIView):
    # 스케줄 목록 API
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user_like_celubs = self.request.user.celebrity_set.all()
        queryset = queryset.filter(celeb__in=user_like_celubs)

        celeb = self.request.GET.getlist('celeb', None)
        date_type = self.request.GET.get('date_type', None)
        req_date = self.request.GET.get('date', None)

        if celeb:
            selected_celubs = Celebrity.objects.filter(id__in=celeb)
            queryset = queryset.filter(celebrity__in=selected_celubs)

        if not date_type and not req_date:
            # filter by today
            queryset = queryset.filter(
                schedule__gte=date.today(),
                schedule__lte=date.today() + timedelta(days=30)
            ).order_by('schedule')
        elif date_type:
            if date_type == 'yesterday':
                queryset = queryset.filter(
                    schedule__date=date.today() - timedelta(days=1))
            elif date_type == 'tomorrow':
                queryset = queryset.filter(
                    schedule__date=date.today() + timedelta(days=1))
            elif date_type == 'week':
                queryset = queryset.filter(
                    schedule__week=date.today().isocalendar()[1]).order_by('schedule')
        elif req_date:
            queryset = queryset.filter(
                schedule__date=datetime.strptime(req_date, "%Y-%m-%d").date())
        else:
            queryset = queryset.none()

        return queryset
