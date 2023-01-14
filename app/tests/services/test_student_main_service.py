from django.test import TestCase, Client
from django.urls import reverse

from app.models import ScholarshipRequest
from app.tests.test_utils import create_student, create_scholarship_request


class StudentHomePageTest(TestCase):
    def setUp(self):
        self.client = Client()
        test_user = 'testuser'
        test_password = 'testpassword'
        self.user = create_student(test_user, test_password)
        self.client.login(username=test_user, password=test_password)
        self.scholar_ship_request = create_scholarship_request(self.user)

    def test_student_home_page_with_approved(self):
        self.scholar_ship_request.status = ScholarshipRequest.APPROVED
        self.scholar_ship_request.save()
        self.assert_response(have_reqeust=True, reqeust_approved=True)

    def test_student_home_page_with_not_approved(self):
        self.scholar_ship_request.status = ScholarshipRequest.REJECTED
        self.scholar_ship_request.save()
        self.assert_response(have_reqeust=True, reqeust_approved=False)

    def test_student_home_page_with_no_request(self):
        self.scholar_ship_request.delete()
        self.assert_response(have_reqeust=False, reqeust_approved=False)

    def assert_response(self, have_reqeust, reqeust_approved):
        response = self.client.get(reverse('student_home_page'))
        # assert that the response is successful
        self.assertEqual(response.status_code, 200)
        # assert that the correct template is used
        self.assertTemplateUsed(response, 'student/home-student.html')
        # assert that the correct context variables are passed to the template
        self.assertEqual(response.context['have_request'], have_reqeust)
        self.assertEqual(response.context['request_approved'], reqeust_approved)
