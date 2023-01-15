from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from app.constants import STUDENT, WORKER


def is_student(user):
    return user.groups.filter(name=STUDENT).exists()


def is_worker(user):
    return user.groups.filter(name=WORKER).exists()


def validate_user(email, pass1, pass2, username, context):
    if User.objects.filter(username=username):
        context["signup_error"] = "Username already exist! Please try some other username."
    if User.objects.filter(email=email).exists():
        context["signup_error"] = "Email Already Registered!!"
    if len(username) > 20:
        context["signup_error"] = "Username must be under 20 charcters!!"
    if pass1 != pass2:
        context["signup_error"] = "Passwords didn't matched!!"
    if not username.isalnum():
        context["signup_error"] = "Username must be Alpha-Numeric!!"


def create_user(email, fname, lname, pass1, pass2, username, context):
    validate_user(email, pass1, pass2, username, context)
    print(context)
    if not context:
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()
        return myuser
    return None


def add_user_to_group(group_name, myuser):
    if myuser is None or group_name is None:
        return
    group_arr = Group.objects.filter(name=group_name)
    if group_arr.exists():
        myuser.groups.add(group_arr[0])


def get_all_students():
    return User.objects.filter(groups__name=STUDENT)