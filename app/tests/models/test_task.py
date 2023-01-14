from django.test import TestCase

from app.models import Task
from app.tests.test_utils import create_student, create_worker


class TaskModelTest(TestCase):
    def setUp(self):
        self.user = create_student()
        self.worker = create_worker()
        self.task = Task.objects.create(
            user_id=self.user,
            worker_id=self.worker,
            place='Test Place',
            total_hours=10,
            completed_hours=5,
            description='Test Description'
        )

    def test_task_creation(self):
        self.assertTrue(isinstance(self.task, Task))
        self.assertEqual(self.task.status, Task.TO_DO)
        self.assertEqual(self.task.user_id, self.user)
        self.assertEqual(self.task.worker_id, self.worker)
        self.assertEqual(self.task.place, 'Test Place')
        self.assertEqual(self.task.total_hours, 10)
        self.assertEqual(self.task.completed_hours, 5)
        self.assertEqual(self.task.description, 'Test Description')

    def test_status_choices(self):
        self.task.status = Task.IN_PROGRESS
        self.task.save()
        self.assertEqual(self.task.status, Task.IN_PROGRESS)

        self.task.status = Task.COMPLETED
        self.task.save()
        self.assertEqual(self.task.status, Task.COMPLETED)
