from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from app.models import ScholarshipRequest
from app.tests.test_utils import get_scholarship_request_form


class SubmitScholarshipRequestTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpassword')

    def test_submit_scholarship_request_success(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('submit_scholarship'), get_scholarship_request_form())
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ScholarshipRequest.objects.count(), 1)

    def test_submit_scholarship_request_failure(self):
        f = get_scholarship_request_form()
        f['volunteer'] = 'off'
        response = self.client.post(reverse('submit_scholarship'), f)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ScholarshipRequest.objects.count(), 0)
