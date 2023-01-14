from django.test import TestCase

from app.services.tasks.tasks_dao import get_tasks, get_task_by_id
from app.tests.test_utils import create_student, create_worker, create_task, delete_tasks


class TaskTests(TestCase):
    def setUp(self):
        self.user = create_student()
        self.worker = create_worker()
        self.task1 = create_task(self.user, self.worker, "task1")
        self.task2 = create_task(self.user, self.worker, "task2")

    def tearDown(self):
        delete_tasks(self.user)

    def test_get_tasks(self):
        tasks = get_tasks(self.user)
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[0], self.task1)
        self.assertEqual(tasks[1], self.task2)

    def test_get_task_by_id(self):
        task = get_task_by_id(self.task1.id)
        self.assertEqual(task, self.task1)

        task = get_task_by_id(999)
        self.assertIsNone(task)
