from calendar import HTMLCalendar
from datetime import datetime as dtime, date, time
import datetime
from .models import Schedule


class ScheduleCalendar(HTMLCalendar):
    def __init__(self, schedules=None):
        super().__init__()
        self.schedules = schedules

    def formatday(self, day, weekday, schedules, theyear, themonth, today, selected):
        schedules_from_day = schedules.filter(schedule__day=day)
        schedules_html = "<ul>"

        celebrities = []
        for schedule in schedules_from_day:
            celebrities.extend(schedule.get_celebrity())
        schedules_html += '<br>'.join(list(set(celebrities)))
        schedules_html += "</ul>"

        print(day, selected.day, today.day)
        if selected.day == day:
            css = 'selected'
        elif today.day == day:
            css = 'today'
        else:
            css = ''

        if day == 0:
            return '<td class="noday">&nbsp;</td>'
        else:
            return """<td class="%s" onclick="window.location.href='?date=%s'"><span>%d</span>%s</td>""" % (
                "%s %s" % (self.cssclasses[weekday], css), '{0}-{1}-{2}'.format(theyear, themonth, day), day, schedules_html)

    def formatweek(self, theweek, schedules, theyear, themonth, today, selected):
        s = ''.join(self.formatday(d, wd, schedules, theyear, themonth, today, selected)
                    for (d, wd) in theweek)
        return '<tr>%s</tr>' % s

    def formatmonth(self, theyear, themonth, today, selected, withyear=True):
        schedules = Schedule.objects.filter(schedule__month=themonth)

        v = []
        a = v.append
        a('<table border="0" cellpadding="0" cellspacing="0" class="month table">')
        a('\n')
        a(self.formatweekheader())
        a('\n')
        for week in self.monthdays2calendar(theyear, themonth):
            a(self.formatweek(week, schedules, theyear, themonth, today, selected))
            a('\n')
        a('</table>')
        a('\n')
        return ''.join(v)
