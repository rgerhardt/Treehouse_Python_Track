from django import template

from courses.models import Course

register = template.Library()

@register.simple_tag
def newest_course():
    return Course.objects.latest('created_at')


@register.inclusion_tag('courses/course_nav.html')
def nav_courses_list():
    courses = Course.objects.all()
    return {'courses': courses}


