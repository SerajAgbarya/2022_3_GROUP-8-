from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from app.services.signIn.signIn import signin
from app.services.signIn.signUp import signup
from members import forms
from . import constants
from .constants import STUDENT_HOME_PAGE
from .services.user.user_dao import is_student
from .tokens import generate_token


def main(request):
    user = request.user
    if user.is_authenticated and is_student(user):
        return redirect(STUDENT_HOME_PAGE)
    return render(request, 'index.html')


def student_signin(request):
    return signin(request, "student/student-signin.html", "./../", constants.STUDENT)


def manager_signin(request):
    return signin(request, "manager-signin.html", "home-manager.html", constants.MANAGER)


def worker_signin(request):
    return signin(request, "worker/worker-signin.html", "worker/home-worker.html", constants.WORKER)


def student_signup(request):
    return signup(request, "student/signup.html", "student_signin", "student/email_confirmation.html",
                  constants.STUDENT)


def worker_signup(request):
    user_form = forms.WorkerUserForm
    worker_form = forms.WorkerForm()
    mydict = {'userForm': user_form, 'workerForm': worker_form}
    if request.method == 'POST':
        user_form = forms.WorkerUserForm(request.POST)
        worker_form = forms.WorkerForm(request.POST, request.FILES)
        if user_form.is_valid() and worker_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.is_active = False
            worker = worker_form.save(commit=False)
            my_worker_group = Group.objects.get(name=constants.WORKER)
            user.groups.add(my_worker_group)
            user.save()
            worker.user = user
            worker = worker.save()
        return redirect('home')
    return render(request, 'workersignup.html', context=mydict)


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        messages.success(request, "Your Email has been Confirmed ,Please wait for admin approval to get access")
        return redirect('student_signin')
    else:
        return render(request, 'activation_failed.html')


def activate_worker(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request, myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('worker_signin')
    else:
        return render(request, 'activation_failed.html')
