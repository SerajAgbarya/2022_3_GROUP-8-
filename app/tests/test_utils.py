from django.contrib.auth.models import User, Group

from app.constants import STUDENT, WORKER, GOOD_SMALL, YES_SMALL, NO_SMALL
from app.models import ScholarshipRequest, Task


def create_student(username='student1', password='student1'):
    user = User.objects.create_user(username=username, password=password)
    user.groups.add(Group.objects.get(name=STUDENT).id)
    return user


def create_worker(username='worker1', password='worker1'):
    user = User.objects.create_user(username=username, password=password)
    user.groups.add(Group.objects.get(name=WORKER).id)
    return user


def create_scholarship_request(user, status=ScholarshipRequest.APPROVED):
    return ScholarshipRequest.objects.create(
        user_id=user,
        degree_year=3,
        age=25,
        financial_situation=GOOD_SMALL,
        parent_work=YES_SMALL,
        special_needs=NO_SMALL,
        tenant=YES_SMALL,
        volunteer=NO_SMALL,
        status=status
    )


def get_scholarship_request_form():
    return {
        'degree_year': '2022',
        'age': '22',
        'financial_situation': 'Good',
        'parent_work': 'Farmer',
        'special_needs': 'None',
        'tenant': 'Yes',
        'volunteer': 'On'
    }


def delete_scholarship_request(user):
    ScholarshipRequest.objects.filter(user_id=user.id).delete()


def create_task(user, worker, description='test desc'):
    return Task.objects.create(
        user_id=user,
        worker_id=worker,
        place='Test Place',
        total_hours=10,
        completed_hours=5,
        description=description
    )


def delete_tasks(user):
    Task.objects.filter(user_id=user.id).delete()
