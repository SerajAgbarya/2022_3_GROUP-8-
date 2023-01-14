from django.test import TestCase
from django.urls import reverse

from app.models import ScholarshipRequest
from app.tests.test_utils import create_student, create_task, create_worker, delete_tasks, create_scholarship_request, \
    delete_scholarship_request

USER_NAME = 'testuser'
PASS = 'testpassword'


class StudentTaskPageTests(TestCase):
    def setUp(self):
        self.user = create_student(USER_NAME, PASS)
        self.worker = create_worker()
        self.task1 = create_task(self.user, self.worker)
        self.task2 = create_task(self.user, self.worker)
        self.client.login(username=USER_NAME, password=PASS)

    def tearDown(self):
        self.client.logout()
        delete_tasks(self.user)
        delete_scholarship_request(self.user)

    def test_student_task_page_view_with_approved_scholarship(self):
        self.scholar_ship_request = create_scholarship_request(self.user)
        response = self.client.get(reverse('student_task'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/student_task.html')
        self.assertEqual(len(response.context['tasks']), 2)
        self.assertEqual(response.context['tasks'][0], self.task1)
        self.assertEqual(response.context['tasks'][1], self.task2)

    def test_student_task_page_view_with_non_approved_scholarship(self):
        self.scholar_ship_request = create_scholarship_request(self.user, ScholarshipRequest.REJECTED)
        response = self.client.get(reverse('student_task'))
        self.assertEqual(response.status_code, 302)

    def test_student_task_page_view_with_no_scholarship(self):
        response = self.client.get(reverse('student_task'))
        self.assertEqual(response.status_code, 302)
