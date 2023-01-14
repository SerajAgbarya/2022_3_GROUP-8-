from datetime import datetime

from django.test import TestCase

from app.services.volunteer.voulnteer_hours_dao import create_new_volunteer_hours, get_volunteer_hours
from app.tests.test_utils import create_task, create_student, create_worker, delete_tasks, create_volunteer_hours

PASSWORD = 'testpassword'
USERNAME = 'testuser'


class VolunteerHoursTestCase(TestCase):
    def setUp(self):
        self.user = create_student(USERNAME, PASSWORD)
        self.worker = create_worker()
        self.task = create_task(self.user, self.worker)

    def tearDown(self):
        delete_tasks(self.user)

    def test_create_new_volunteer_hours(self):
        date = '2022-01-01'
        hours = 4
        volunteer_hours = create_new_volunteer_hours(date, hours, self.task, self.user)
        self.assertIsNotNone(volunteer_hours)
        self.assertEqual(volunteer_hours.date, date)
        self.assertEqual(volunteer_hours.hours, hours)
        self.assertEqual(volunteer_hours.task_id, self.task)
        self.assertEqual(volunteer_hours.user_id, self.user)

    def test_create_new_volunteer_hours_with_missing_args(self):
        hours = 4
        volunteer_hours = create_new_volunteer_hours(None, hours, self.task, self.user)
        self.assertIsNone(volunteer_hours)

    def test_get_volunteer_hours(self):
        date = datetime.now().date()
        hours = 4
        create_volunteer_hours(self.user, self.task, date, hours)
        volunteer_hours = get_volunteer_hours(self.user)
        self.assertEqual(len(volunteer_hours), 1)
        self.assertEqual(volunteer_hours[0].date, date)
        self.assertEqual(volunteer_hours[0].hours, hours)
        self.assertEqual(volunteer_hours[0].task_id, self.task)
        self.assertEqual(volunteer_hours[0].user_id, self.user)

    def test_get_volunteer_hours_with_none_user(self):
        volunteer_hours = get_volunteer_hours(None)
        self.assertEqual(len(volunteer_hours), 0)
