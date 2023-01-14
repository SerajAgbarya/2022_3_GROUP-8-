from django.contrib.auth.models import User, Group

from app.constants import STUDENT, WORKER


def create_student(username='student1', password='student1'):
    user = User.objects.create_user(username=username, password=password)
    user.groups.add(Group.objects.get(name=STUDENT).id)
    return user


def create_worker(username='worker1', password='worker1'):
    user = User.objects.create_user(username=username, password=password)
    user.groups.add(Group.objects.get(name=WORKER).id)
    return user
