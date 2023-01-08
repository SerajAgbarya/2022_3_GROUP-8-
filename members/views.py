from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader

from cdfi import settings


@login_required
def index(request):
    template = loader.get_template('first.html')
    return render(request, 'first.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Login success  "))
            # Redirect to a success page.
            return render(request, 'first.html')

        else:
            # Return an 'invalid login' error message. stay on the same page
            messages.success(request, ("There was An Error Logging In , try Again...  "))
            return render(request, 'login.html')
    else:
        template = loader.get_template('login.html')
        return HttpResponse(template.render({}, request))


@login_required
def logout_user(request):
    logout(request)
    return redirect('login_user')


@login_required
def worker_list(request):
    all_users = User.objects.all()
    workers = []
    group = Group.objects.get(name='worker')
    for user in all_users:
        if user.is_active != True and group in user.groups.all():
            workers.append(user)

    if request.method == 'POST':
        action = request.POST['action']
        user_id = request.POST['user_id']
        user = User.objects.get(pk=user_id)
        if action == 'activate':
            user.is_active = True
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
    group = Group.objects.get(name='worker')
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
            message = "Hello " + user.first_name + "!! \n" + "Welcome to CDFI system! \nThank you for Working with us\n. We have sent you a salay for this month.\nPleas check your acount in the bank."
            from_email = settings.EMAIL_HOST_USER
            to_list = [user.email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            messages.success(request, (f"money has been transfered"))

        return HttpResponseRedirect(request.path_info)

    context = {'users': active}
    return render(request, 'transfer_worker.html', context)


def delete_worker(request):
    all_users = User.objects.all()
    workers = []
    active = []
    group = Group.objects.get(name='worker')
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
        if action == 'delete':
            user.delete()
            messages.success(request, (f"{user.username} has been deleted"))

        return HttpResponseRedirect(request.path_info)

    context = {'users': active}
    return render(request, 'delete_worker.html', context)


def logout_worker(request):
    logout(request)
    messages.success(request, ("You , Were logged out...  "))
    return redirect('worker_login')


def worker_login(request):
    print("dfsdfsdf")
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
            return render(request, 'login.html')
    else:
        template = loader.get_template('login.html')
        return HttpResponse(template.render({}, request))
