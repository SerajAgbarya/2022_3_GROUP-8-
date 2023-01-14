from datetime import datetime

from django.test import TestCase
from django.urls import reverse

from app.models import ScholarshipRequest, VolunteerHours
from app.tests.test_utils import create_student, create_worker, create_task, create_scholarship_request, \
    delete_all_user_info, create_volunteer_hours

PASSWORD = 'testpassword'

USERNAME = 'testuser'


class VolunteerViewsTestCase(TestCase):
    def setUp(self):
        self.user = create_student(USERNAME, PASSWORD)
        self.worker = create_worker()
        self.task = create_task(self.user, self.worker)
        self.client.login(username=USERNAME, password=PASSWORD)

    def tearDown(self):
        self.client.logout()
        delete_all_user_info(self.user)

    def call_service(self):
        return self.client.get(reverse('student_volunteer'))

    def call_post_service(self, body):
        return self.client.post(reverse('student_save_volunteer'), body)

    def test_student_volunteer_page(self):
        self.scholarship = create_scholarship_request(self.user)
        self.volunteer_hours_date = datetime(2022, 1, 1).date()
        self.volunteer_hours_hours = 4
        self.volunteer_hours = create_volunteer_hours(self.user, self.task, self.volunteer_hours_date,
                                                      self.volunteer_hours_hours)

        response = self.call_service()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/student_volunteer.html')
        self.assertEqual(response.context['tasks'][0], self.task)
        self.assertEqual(response.context['volunteer_hours_list'][0], self.volunteer_hours)

    def test_student_volunteer_page_with_unapproved_request(self):
        create_scholarship_request(self.user, ScholarshipRequest.PENDING)
        response = self.call_service()
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/student/')

    def test_student_save_volunteer(self):
        self.scholarship = create_scholarship_request(self.user)
        body = {'date': '2022-01-01', 'hours': 4, 'task': self.task.id}
        response = self.call_post_service(body)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/student/volunteer/')
        volunteer_hours = VolunteerHours.objects.get(user_id=self.user, task_id=self.task)
        self.assertEqual(str(volunteer_hours.date)[:10], '2022-01-01')
        self.assertEqual(volunteer_hours.hours, 4)
        self.assertEqual(volunteer_hours.task_id, self.task)
        self.assertEqual(volunteer_hours.user_id, self.user)

    def test_student_save_volunteer_with_unapproved_request(self):
        create_scholarship_request(self.user, ScholarshipRequest.PENDING)
        response = self.call_post_service({'date': '2022-01-01', 'hours': 4, 'task': self.task.id})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/student/')
