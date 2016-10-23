from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone

from .models import Course, Step


class CourseModelsTests(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            title='Python Regular Course',
            description='Learn to write regular expressions',
        )

        now = timezone.now()
        self.assertLess(course.created_at, now)


class CourseViewsTests(TestCase):

    def setUp(self):
        self.course1 = Course.objects.create(
            title='Test Course',
            description='Learn to write tests',
        )
        self.course2 = Course.objects.create(
            title='New Course',
            description='A new course',
        )
        self.step = Step.objects.create(
            title='Introduction to doctests',
            description='Learn to write doctests',
            course=self.course1
        )

    def test_course_list_view(self):
        resp = self.client.get(reverse('courses:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.course1, resp.context['courses'])
        self.assertIn(self.course2, resp.context['courses'])
        self.assertTemplateUsed(resp, 'courses/course_list.html')
        self.assertContains(resp, self.course1.title)

    def test_course_detail_view(self):
        resp = self.client.get(reverse('courses:detail', kwargs={'pk': self.course1.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.course1, resp.context['course'])
