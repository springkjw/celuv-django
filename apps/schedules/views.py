import datetime
import calendar
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.safestring import mark_safe
from django.utils import timezone
from django.urls import reverse_lazy

from .calendar import ScheduleCalendar
from .models import Schedule
from .forms import ScheduleForm


class ScheduleMonthlyView(ListView):
    template_name = 'schedule/month.html'
    queryset = Schedule.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        date = self.request.GET.get('date')
        if date:
            repay_datetime = datetime.datetime.strptime(date, '%Y-%m-%d')
            repay_datetime_aware = timezone.make_aware(repay_datetime).date()
            queryset = queryset.filter(
                schedule__year=repay_datetime_aware.year,
                schedule__month=repay_datetime_aware.month,
                schedule__day=repay_datetime_aware.day
            )
        else:
            queryset = queryset.filter(
                schedule__year=timezone.now().date().year,
                schedule__month=timezone.now().date().month,
                schedule__day=timezone.now().date().day,
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = datetime.date.today()
        date = self.request.GET.get('date')
        if date:
            date = timezone.make_aware(
                datetime.datetime.strptime(date, '%Y-%m-%d'))
        else:
            date = timezone.now()
        cal = ScheduleCalendar(calendar.SUNDAY)
        html_calendar = cal.formatmonth(
            d.year, d.month, d, date, withyear=False)
        html_calendar = html_calendar.replace(
            '<td ', '<td ')

        context.update({
            'calendar': mark_safe(html_calendar),
            'date': date
        })
        return context


class ScheduleCreateView(CreateView):
    template_name = 'schedule/create.html'
    queryset = Schedule.objects.all()
    form_class = ScheduleForm
    success_url = reverse_lazy('schedule:month')


class ScheduleDetailView(UpdateView):
    template_name = 'schedule/update.html'
    model = Schedule
    form_class = ScheduleForm
    success_url = reverse_lazy('schedule:month')


class ScheduleDeleteView(DeleteView):
    model = Schedule
    success_url = reverse_lazy('schedule:month')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)