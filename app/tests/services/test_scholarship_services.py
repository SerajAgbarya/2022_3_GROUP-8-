from django.test import TestCase
from django.urls import reverse

from app.models import ScholarshipRequest
from app.tests.test_utils import get_scholarship_request_form, delete_scholarship_request, create_student

PASSWORD = 'testpassword'
USER_NAME = 'testuser'


class SubmitScholarshipRequestTest(TestCase):
    def setUp(self):
        self.user = create_student(USER_NAME, PASSWORD)
        self.client.login(username=USER_NAME, password=PASSWORD)

    def tearDown(self):
        delete_scholarship_request(self.user)
        self.client.logout()

    def test_submit_scholarship_request_success(self):
        response = self.client.post(reverse('submit_scholarship'), get_scholarship_request_form())
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ScholarshipRequest.objects.count(), 1)
        delete_scholarship_request(self.user)

    def test_submit_scholarship_request_failure(self):
        f = get_scholarship_request_form()
        f['volunteer'] = 'off'
        response = self.client.post(reverse('submit_scholarship'), f)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ScholarshipRequest.objects.count(), 0)

    def test_scholarship_form_request_view(self):
        response = self.client.get(reverse('scholarship_form_request_view'))

        # Assert that the request was successful
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template was used
        self.assertTemplateUsed(response, 'student/scholarship-form.html')

        # Assert that the context contains the expected variables
        self.assertIn('DEGREE_YEAR_CHOICES', response.context)
        self.assertIn('FINANCIAL_SITUATION_CHOICES', response.context)
        self.assertIn('YES_NO_CHOICES', response.context)

    def test_scholarship_view_and_edit(self):
        response = self.client.get(reverse('scholarship_view_edit'))

        # Assert that the request was successful
        self.assertEqual(response.status_code, 200)

        # Assert that the correct template was used
        self.assertTemplateUsed(response, 'student/scholarship-form-view.html')

        # Assert that the context contains the expected variables
        self.assertIn('request', response.context)
        self.assertEqual(response.context['request'], None)
        self.assertIn('DEGREE_YEAR_CHOICES', response.context)
        self.assertIn('FINANCIAL_SITUATION_CHOICES', response.context)
        self.assertIn('YES_NO_CHOICES', response.context)
