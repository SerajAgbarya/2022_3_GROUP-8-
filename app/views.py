from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from .signIn.signIn import signin
from .signIn.signUp import signup
from .tokens import generate_token


def main(request):
    return render(request, 'index.html')


def student_signin(request):
    return signin(request, "student/student-signin.html", "student/home-student.html")


def manager_signin(request):
    return signin(request, "manager-signin.html", "home-manager.html")


def worker_signin(request):
    return signin(request, "worker/worker-signin.html", "worker/home-worker.html")


def student_signup(request):
    return signup(request, "student/signup.html", "student_signin", "student/email_confirmation.html")


def worker_signup(request):
    return signup(request, "worker/signup.html", "worker_signin", "worker/email_confirmation.html")


def activate(request, uidb64, token):
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
