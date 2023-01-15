from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.test import TestCase
import unittest
from django.test import RequestFactory

from app import constants
from members.views import index
from django.contrib.auth.models import User, Group
from django.test import Client
from .models import Worker


class ManagerLoginTest(TestCase):

    def setUp(self):
        # setup function run before each test
        self.user_manager = get_user_model().objects.create_user(username='test_user', password='12test12',
                                                                 email='test@example.com')
        group, created = Group.objects.get_or_create(name=constants.MANAGER)
        self.user_manager.groups.add(group)
        self.user_manager.save()
        self.user_worker = get_user_model().objects.create_user(username='test_user_worker', password='12test12',
                                                                email='worker_test@example.com', is_active=False)
        group, created = Group.objects.get_or_create(name=constants.WORKER)
        self.user_worker.groups.add(group)
        self.user_worker.save()
        self.client = Client(enforce_csrf_checks=True)

    def tearDown(self):
        # run after test
        self.user_manager.delete()

    def test_correct(self):
        user = authenticate(username='test_user', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='test_user', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_login_user(self):
        response = self.client.get('/members/login_user')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        csrf_token = response.cookies['csrftoken'].value
        response = self.client.post('/members/login_user', data={'username': 'test_user', 'password': '12test12'},
                                    HTTP_X_CSRFTOKEN=csrf_token)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'first.html')

    def test_logout_user(self):
        self.manager_login()
        response = self.client.get('/members/logout_user')
        self.assertEqual(response.status_code, 302)

    def manager_login(self):
        response = self.client.get('/members/login_user')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.csrf_token = response.cookies['csrftoken'].value
        response = self.client.post('/members/login_user', data={'username': 'test_user', 'password': '12test12'},
                                    HTTP_X_CSRFTOKEN=self.csrf_token)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'first.html')
        print('Login success')

    def test_add_user(self):
        self.manager_login()
        response = self.client.get('/members/worker_list')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'worker_list.html')

    def test_delete_user(self):
        self.manager_login()
        response = self.client.get('/members/delete_worker')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_worker.html')

    def test_transfer(self):
        self.manager_login()
        response = self.client.get('/members/transfer_to_worker')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'transfer_worker.html')

    def test_money_request(self):
        self.manager_login()
        response = self.client.get('/members/money_request')
        self.assertEqual(response.status_code, 200)

    def test_worker_details(self):
        self.manager_login()
        response = self.client.get('/members/worker_details')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'worker_details.html')

    def test_worker_login(self):
        response = self.client.get('/members/worker_login')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'worker-sign-in.html')
        self.csrf_token = response.cookies['csrftoken'].value
        response = self.client.post('/members/worker_login', data={'username': 'test_user', 'password': '12test12'},
                                    HTTP_X_CSRFTOKEN=self.csrf_token)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home-worker.html')
        print('Login success')

    def worker_login(self):
        response = self.client.get('/members/worker_login')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'worker-sign-in.html')
        self.csrf_token = response.cookies['csrftoken'].value

        response = self.client.post('/members/worker_login', data={'username': 'test_user', 'password': '12test12'},
                                    HTTP_X_CSRFTOKEN=self.csrf_token)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home-worker.html')
        print('Login success')

    def test_add_students(self):
        self.worker_login()
        response = self.client.get('/members/student_list')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student_list.html')

    def test_worker_tasks(self):
        self.worker_login()
        response = self.client.get('/members/worker_tasks')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'worker_tasks.html')

    def test_accept_scholarship(self):
        self.worker_login()
        response = self.client.get('/members/accept_scholarship')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scholarship_requests.html')

    def test_delete_student(self):
        self.worker_login()
        response = self.client.get('/members/delete_student')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_student.html')

    def test_logout_worker(self):
        self.worker_login()
        response = self.client.get('/members/worker_logout')
        self.assertEqual(response.status_code, 302)

    def test_sign_up(self):
        response = self.client.get('/worker-signup')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workersignup.html')

    def test_worker_home_page(self):
        response = self.client.get('/members/home_pageworker')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home-worker.html')
