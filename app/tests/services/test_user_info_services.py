from django.test import TestCase
from django.urls import reverse

from app.constants import STUDENT_HOME_PAGE
from app.tests.test_utils import create_student

PASSWORD = 'testpassword'

USERNAME = 'testuser'


class EditStudentPersonalInfoTestCase(TestCase):
    def setUp(self):
        self.user = create_student(USERNAME, PASSWORD)
        self.user.first_name = "Test"
        self.user.last_name = "User"
        self.user.save()
        self.client.login(username=USERNAME, password=PASSWORD)

    def test_edit_student_personal_info(self):
        # make a POST request to the edit_student_personal_info view
        response = self.client.post(reverse('edit_student_personal_info'), {
            'fname': 'New Test',
            'lname': 'New User',
            'pass1': 'newpassword',
            'pass2': 'newpassword'
        })

        self.assertRedirects(response, STUDENT_HOME_PAGE, status_code=302, target_status_code=302)
        # check that the user's first name and last name were updated
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'New Test')
        self.assertEqual(self.user.last_name, 'New User')
        # check that the user's password was updated
        self.assertTrue(self.user.check_password('newpassword'))

    def test_get_student_personal_info_page(self):
        # make a POST request to the edit_student_personal_info view
        response = self.client.get(reverse('edit_student_personal_info'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/edit_user_info.html')
