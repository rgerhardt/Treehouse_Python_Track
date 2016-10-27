from django import template

from courses.models import Course

register = template.Library()

@register.simple_tag
def newest_course():
    return Course.objects.latest('created_at')