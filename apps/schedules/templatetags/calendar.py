import datetime
import calendar
from django import template 

register = template.Library()


@register.filter
def get_next_month(date):
    month = date.month
    year = date.year + month // 12
    month = month % 12 + 1
    day = min(date.day, calendar.monthrange(year, month)[1])
    return datetime.datetime.strftime(
        datetime.date(year, month, day), '%Y-%m-%d')


@register.filter
def get_prev_month(date):
    month = date.month - 2
    year = date.year + month // 12
    month = month % 12 + 1
    day = min(date.day, calendar.monthrange(year, month)[1])
    return datetime.datetime.strftime(
        datetime.date(year, month, day), '%Y-%m-%d')