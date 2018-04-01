import datetime
from django.views.generic import TemplateView, CreateView
from django.utils.safestring import mark_safe
from django.urls import reverse_lazy

from .calendar import ScheduleCalendar
from .models import Schedule
from .forms import ScheduleForm


class ScheduleMonthlyView(TemplateView):
    template_name = 'schedule/month.html'

    def get_context_data(self, **kwargs):
        d = datetime.date.today()
        cal = ScheduleCalendar()
        html_calendar = cal.formatmonth(d.year, d.month, withyear=True)
        html_calendar = html_calendar.replace(
            '<td ', '<td ')
        context = {
            'calendar': mark_safe(html_calendar)
        }

        return context


class ScheduleCreateView(CreateView):
    template_name = 'schedule/create.html'
    queryset = Schedule.objects.all()
    form_class = ScheduleForm
    success_url = reverse_lazy('schedule:month')
