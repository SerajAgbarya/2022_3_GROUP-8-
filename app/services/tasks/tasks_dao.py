from datetime import datetime

from app.models import Task


def get_tasks(user):
    return Task.objects.filter(user_id=user.id)


def get_task_by_id(task_id):
    try:
        return Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return None


def progress_task(task, hours):
    if task is None or hours is None or not hours.isdigit or int(hours) < 0:
        return
    task.completed_hours += int(hours)
    if task.status == Task.TO_DO:
        task.status = Task.IN_PROGRESS
    if task.completed_hours >= task.total_hours:
        task.status = Task.COMPLETED
    now = datetime.now()
    task.created_at = now
    task.updated_at = now
    task.save()


def create_task(worker, user, place, total_hours, description):
    task = Task()
    task.user_id = user
    task.worker_id = worker
    task.status = Task.TO_DO
    task.place = place
    task.total_hours = total_hours
    task.completed_hours = 0
    task.description = description
    task.save()
