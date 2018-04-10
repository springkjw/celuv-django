from django import template

from apps.celebritys.models import Celebrity

register = template.Library()


@register.simple_tag
def get_manager(object):
    return Celebrity.objects.filter(entertainment__in=[object]).count()
