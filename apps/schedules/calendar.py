from calendar import HTMLCalendar
from datetime import datetime as dtime, date, time
import datetime
from .models import Schedule


class ScheduleCalendar(HTMLCalendar):
    def __init__(self, schedules=None):
        super().__init__()
        self.schedules = schedules

    def formatday(self, day, weekday, schedules):
        schedules_from_day = schedules.filter(schedule__day=day)
        schedules_html = "<ul>"

        celebrities = []
        for schedule in schedules_from_day:
            celebrities.extend(schedule.get_celebrity())
        schedules_html += '<br>'.join(list(set(celebrities)))
        schedules_html += "</ul>"

        if day == 0:
            return '<td class="noday">&nbsp;</td>'
        else:
            return '<td class="%s">%d%s</td>' % (
                self.cssclasses[weekday], day, schedules_html)

    def formatweek(self, theweek, schedules):
        s = ''.join(self.formatday(d, wd, schedules) for (d, wd) in theweek)
        return '<tr>%s</tr>' % s

    def formatmonth(self, theyear, themonth, withyear=True):
        schedules = Schedule.objects.filter(schedule__month=themonth)

        v = []
        a = v.append
        a('<table border="0" cellpadding="0" cellspacing="0" class="month table">')
        a('\n')
        a(self.formatmonthname(theyear, themonth, withyear=withyear))
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week, schedules))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)
