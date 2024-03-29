import json

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader

from app.services.tasks.tasks_dao import get_tasks, create_task
from app.services.user.user_dao import get_all_students
from cdfi import settings
from .forms import WorkHoursForm
from .models import WorkHours
from .models import Worker
from app.models import ScholarshipRequest


@login_required
def index(request):
    template = loader.get_template('first.html')
    return render(request, 'first.html')


def login_user(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        all_users = User.objects.all()
        manager = []
        group = Group.objects.get(name='MANGER')

        if user is not None:
            if group in user.groups.all():
                login(request, user)
                messages.success(request, ("Login success  "))
                # Redirect to a success page.
                return render(request, 'first.html')
            else:
                context["login_error"] = f"You dont have permission to login as Manager"
                template = loader.get_template('login.html')
                return HttpResponse(template.render(context, request))
        else:
            # Return an 'invalid login' error message. stay on the same page
            context["login_error"] = "Bad Credentials!!"
            # messages.success(request, ("There was An Error Logging In , try Again...  "))
            # return render(request, 'login.html')
            template = loader.get_template('login.html')
            return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('login.html')
        return HttpResponse(template.render(context, request))


@login_required
def logout_user(request):
    logout(request)
    return redirect('login_user')


@login_required
def worker_list(request):
    all_users = User.objects.all()
    workers = []
    group = Group.objects.get(name='WORKER')
    for user in all_users:
        if user.is_active != True and group in user.groups.all():
            workers.append(user)

    if request.method == 'POST':
        action = request.POST['action']
        user_id = request.POST['user_id']
        user = User.objects.get(pk=user_id)
        if action == 'activate':
            user.is_active = True
            subject = "Accepted for the work in CDFI Bank!"
            message = "Hello " + user.first_name + "!! \n" + "Welcome to CDFI system! \n You now worker in CDFI Bank. \n You can to enter to the website as a worker ."
            from_email = settings.EMAIL_HOST_USER
            to_list = [user.email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            user.save()
            messages.success(request, (f"{user.username} has been activated"))

        return HttpResponseRedirect(request.path_info)

    context = {'users': workers}
    return render(request, 'worker_list.html', context)


@login_required
def transfer_to_worker(request):
    all_users = User.objects.all()
    workers = []
    active = []
    group = Group.objects.get(name='WORKER')
    for user in all_users:
        if group in user.groups.all():
            workers.append(user)
    for worker in workers:
        if worker.is_active == True:
            active.append(worker)

    if request.method == 'POST':
        action = request.POST['action']
        user_id = request.POST['user_id']
        user = User.objects.get(pk=user_id)
        if action == 'transfer':
            subject = "Salary!"
            message = "Hello " + user.first_name + "!! \n" + "Welcome to CDFI system! \nThank you for Working with us\n. We have sent you a salay for this month.\nPleas check your acount."
            from_email = settings.EMAIL_HOST_USER
            to_list = [user.email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            messages.success(request, (f"money has been transfered to " + user.first_name + " " + user.last_name))

        return HttpResponseRedirect(request.path_info)

    context = {'users': active}
    return render(request, 'transfer_worker.html', context)


def delete_worker(request):
    all_workers = Worker.objects.all()
    workers = []
    active = []
    for worker in all_workers:
        workers.append(worker)
    for worker in workers:
        if worker.user.is_active == True:
            active.append(worker)
    if request.method == 'POST':
        action = request.POST['action']
        user_id = request.POST['user_id']
        user = User.objects.get(pk=user_id)
        for worker in Worker.objects.all():
            if worker.user.pk == user_id:
                worker.delete()
        if action == 'delete':
            subject = "Block from the CDFI Bank !!!"
            message = "Hello " + user.first_name + "!! \n" + "Thank you for Working with us\n. You have ben deleted from our system."
            from_email = settings.EMAIL_HOST_USER
            to_list = [user.email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            user.delete()

            messages.success(request, (f"{user.username} has been deleted"))

        return HttpResponseRedirect(request.path_info)

    context = {'workers': active}
    return render(request, 'delete_worker.html', context)


def worker_details(request):
    all_workers = Worker.objects.all()
    workers = []
    active = []
    for worker in all_workers:
        workers.append(worker)
    for worker in workers:
        if worker.user.is_active == True:
            active.append(worker)
    context = {'workers': active}
    return render(request, 'worker_details.html', context)


def money_request(request):
    manager_user = request.user
    email = manager_user.email
    subject = "According for money request !!!"
    message = "Hello  !! \n" + "the request was accepted ! "
    from_email = settings.EMAIL_HOST_USER
    to_list = [email]
    send_mail(subject, message, from_email, to_list, fail_silently=True)
    messages.success(request, (f"the request was sent at the e_mail...please check your email"))
    return render(request, 'first.html')

    return HttpResponseRedirect(request, request.path_info)


def logout_worker(request):
    logout(request)
    messages.success(request, ("You , Were logged out...  "))
    return redirect('worker_login')


def home_pageworker(request):
    return render(request, 'home-worker.html')


def worker_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Login success  "))
            # Redirect to a success page.
            return render(request, 'home-worker.html')

        else:
            # Return an 'invalid login' error message. stay on the same page
            messages.success(request, ("There was An Error Logging In , try Again...  "))
            return render(request, 'worker-sign-in.html')
    else:
        template = loader.get_template('worker-sign-in.html')
        return HttpResponse(template.render({}, request))


def student_list(request):
    all_users = User.objects.all()
    students = []
    group = Group.objects.get(name='STUDENT')
    for user in all_users:
        if user.is_active != True and group in user.groups.all():
            students.append(user)
    if request.method == 'POST':
        action = request.POST['action']
        user_id = request.POST['user_id']
        user = User.objects.get(pk=user_id)
        if action == 'activate':
            user.is_active = True
            subject = "Accepted for CDFI Bank!"
            message = "Hello " + user.first_name + "!! \n" + "Welcome to CDFI system! \n You now active in CDFI Bank. \n You can to enter to the website as a STUDENT ."
            from_email = settings.EMAIL_HOST_USER
            to_list = [user.email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            user.save()
            messages.success(request, (f"{user.username} has been activated"))

        return HttpResponseRedirect(request.path_info)

    context = {'students': students}
    return render(request, 'student_list.html', context)


def delete_student(request):
    all_users = User.objects.all()
    students = []
    group = Group.objects.get(name='STUDENT')
    for user in all_users:
        if group in user.groups.all():
            students.append(user)

    if request.method == 'POST':
        action = request.POST['action']
        user_id = request.POST['user_id']
        user = User.objects.get(pk=user_id)
        if action == 'delete':
            subject = "Block from the CDFI Bank !!!"
            message = "Hello " + user.first_name + "!! \n" + "sorry for ! \nThank you \n. you have deleted from CDFI system ."
            from_email = settings.EMAIL_HOST_USER
            to_list = [user.email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            user.delete()
            messages.success(request, (f"{user.username} has been deleted"))

        return HttpResponseRedirect(request.path_info)
    context = {'students': students}
    return render(request, 'delete_student.html', context)


def add_workhours(request):
    if request.method == 'POST':
        form = WorkHoursForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_workhours')
    else:
        form = WorkHoursForm()
    return render(request, 'add_workhours.html', {'form': form})


def view_workhours(request):
    workhours_list = WorkHours.objects.all()
    return render(request, 'view_workhours.html', {'workhours_list': workhours_list})


def delete_workhours(request, pk):
    WorkHours.objects.filter(pk=pk).delete()
    return redirect('view_workhours')


@login_required
def worker_tasks(request):
    worker = request.user
    students_users = get_all_students()
    students = []
    for student_user in students_users:
        student = {
            'username': student_user.username,
            'id': student_user.id
        }
        students.append(student)
    html_page = 'worker_tasks.html'
    student_id = request.GET.get('student_id')
    if student_id is not None and request.method == 'POST':
        student_tasks = get_tasks(User.objects.get(id=int(student_id)))
        res = []
        for t in student_tasks :
            res.append({
                'id': t.id,
                'description': t.description,
                'place': t.place,
                'total_hours': t.total_hours,
                'completed_hours': t.completed_hours,
                'status': t.status,
            })
        print(res)
        return HttpResponse(json.dumps(res), content_type='application/json')

    if request.method == 'POST' and student_id is None:
        student = request.POST['student_id']
        description = request.POST['description']
        place = request.POST['place']
        hours = request.POST['hours']
        create_task(worker, User.objects.get(id=student), place, hours, description)
        return redirect('worker_tasks')

    return render(request, html_page, {'students': students})



def scholarship_requests(request):
    # Retrieve all the scholarship requests
    scholarship_requests = ScholarshipRequest.objects.all()

    if request.method == 'POST':
        # Get the selected scholarship request ID
        request_id = request.POST.get('request_id')

        # Get the selected action (accept or reject)
        action = request.POST.get('action')

        # Get the selected scholarship request
        scholarship_request = ScholarshipRequest.objects.get(id=request_id)

        if action == 'accept':
            scholarship_request.status = ScholarshipRequest.APPROVED
            scholarship_request.save()
        elif action == 'reject':
            scholarship_request.status = ScholarshipRequest.REJECTED
            scholarship_request.save()
        elif action == 'under_review':
            scholarship_request.status = ScholarshipRequest.UNDER_REVIEW
            scholarship_request.save()

    return render(request, 'scholarship_requests.html', {'scholarship_requests': scholarship_requests})
