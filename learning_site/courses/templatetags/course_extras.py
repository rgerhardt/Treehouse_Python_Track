from django import template
from django.utils.safestring import mark_safe

import markdown2

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

@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)