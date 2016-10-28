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

@register.filter('time_estimate')
def time_estimate(word_count):
    minutes = round(word_count/20)
    return minutes