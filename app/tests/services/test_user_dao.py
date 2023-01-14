from django.contrib.auth.models import User, Group
from django.test import TestCase

from app.constants import STUDENT, WORKER
from app.services.user.user_dao import create_user, validate_user, is_student, is_worker, add_user_to_group


class UserTestCase(TestCase):
    def test_create_user(self):
        # create test data
        email = 'test@example.com'
        fname = 'Test'
        lname = 'User'
        pass1 = 'password123'
        pass2 = 'password123'
        username = 'testuser'
        context = {}

        # call the create_user function
        myuser = create_user(email, fname, lname, pass1, pass2, username, context)

        # assert that the user was created successfully
        self.assertIsNotNone(myuser)
        self.assertEqual(myuser.email, email)
        self.assertEqual(myuser.first_name, fname)
        self.assertEqual(myuser.last_name, lname)
        self.assertFalse(myuser.is_active)

    def test_create_user(self):
        # create test data
        email = 'test@example.com'
        fname = 'Test'
        lname = 'User'
        pass1 = 'password123'
        pass2 = 'password123'
        username = 'testuser'
        context = {}

        # call the create_user function
        myuser = create_user(email, fname, lname, pass1, pass2, username, context)

        # assert that the user was created successfully
        self.assertIsNotNone(myuser)
        self.assertEqual(myuser.email, email)
        self.assertEqual(myuser.first_name, fname)
        self.assertEqual(myuser.last_name, lname)
        self.assertFalse(myuser.is_active)

    def test_validate_user(self):
        # create test data
        email = 'test@example.com'
        pass1 = 'password123'
        pass2 = 'password123'
        username = 'testuser'
        context = {}

        # call the validate_user function
        validate_user(email, pass1, pass2, username, context)

        # assert that there are no errors in the context dictionary
        self.assertEqual(context, {})

    def test_is_student(self):
        # create test user and add them to the STUDENT group
        myuser = User.objects.create_user('testuser', 'test@example.com', 'password123')
        student_group = Group.objects.get(name=STUDENT)
        myuser.groups.add(student_group)

        # call the is_student function and assert that it returns True
        self.assertTrue(is_student(myuser))

    def test_is_worker(self):
        # create test user and add them to the WORKER group
        myuser = User.objects.create_user('testuser', 'test@example.com', 'password123')
        worker_group = Group.objects.get(name=WORKER)
        myuser.groups.add(worker_group)

        # call the is_worker function and assert that it returns True
        self.assertTrue(is_worker(myuser))

    def test_add_user_to_group(self):
        # create test user and group
        myuser = User.objects.create_user('testuser', 'test@example.com', 'password123')
        test_group = Group.objects.create(name='testgroup')

        # call the add_user_to_group function
        add_user_to_group('testgroup', myuser)

        # assert that the user is now in the test group
        self.assertTrue(myuser.groups.filter(name='testgroup').exists())
