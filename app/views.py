from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from .scholarship.scholarship_crud import submit_scholarship_reqeust, get_scholarship_reqeust
from .signIn.signIn import signin
from .signIn.signUp import signup
from .tokens import generate_token
from members import forms, models
from django.http import HttpResponseRedirect
from members import urls
from django.contrib.auth.models import Group





def main(request):
    return render(request, 'index.html')


def student_signin(request):
    return signin(request, "student/student-signin.html", "student/home/", "student")


def manager_signin(request):
    return signin(request, "manager-signin.html", "home-manager.html", "manager")


def worker_signin(request):
    return signin(request, "worker/worker-signin.html", "worker/home-worker.html", "worker")


def student_signup(request):
    return signup(request, "student/signup.html", "student_signin", "student/email_confirmation.html", "student")


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
            user.save()
            worker = worker_form.save(commit=False)
            worker.user = user
            worker = worker.save()
            my_worker_group = Group.objects.get_or_create(name='WORKER')
            my_worker_group[0].user_set.add(user)
        return redirect('home')
    return render(request, 'workersignup.html', context=mydict)

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


def submit_scholarship(request):
    return submit_scholarship_reqeust(request)


def scholarship_form(request):
    degree_year_choices = [(i, str(i)) for i in range(1, 5)]
    financial_situation_choices = [('bad', 'Bad'), ('mid', 'Mid'), ('good', 'Good')]
    yes_no_choices = [('yes', 'Yes'), ('no', 'No')]
    return render(request, 'student/scholarship-form.html', {
        'DEGREE_YEAR_CHOICES': degree_year_choices,
        'FINANCIAL_SITUATION_CHOICES': financial_situation_choices,
        'YES_NO_CHOICES': yes_no_choices,
    })


def scholarship_view(request):
    return get_scholarship_reqeust(request)


def student_home_page(request):
    student_name = request.user.first_name.capitalize()
    return render(request, 'student/home-student.html', {'student_name': student_name})


