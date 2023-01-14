from datetime import date

from django.test import TestCase

from app.models import Task, VolunteerHours
from app.tests.test_utils import create_student, create_worker


class VolunteerHoursModelTest(TestCase):
    def setUp(self):
        self.student = create_student()
        self.worker = create_worker()
        self.task = Task.objects.create(
            user_id=self.student,
            worker_id=self.worker,
            place='Test Place',
            total_hours=10,
            completed_hours=5,
            description='Test Description'
        )
        self.volunteer_hours = VolunteerHours.objects.create(
            user_id=self.student,
            task_id=self.task,
            date=date.today(),
            hours=5
        )

    def test_volunteer_hours_creation(self):
        self.assertTrue(isinstance(self.volunteer_hours, VolunteerHours))
        self.assertEqual(self.volunteer_hours.user_id, self.student)
        self.assertEqual(self.volunteer_hours.task_id, self.task)
        self.assertEqual(self.volunteer_hours.date, date.today())
        self.assertEqual(self.volunteer_hours.hours, 5)
