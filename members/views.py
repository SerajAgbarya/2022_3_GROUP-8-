from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


def index(request):
    template = loader.get_template('first.html')
    return HttpResponse(template.render())


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


def logout_user(request):
    logout(request)
    messages.success(request, ("You , Were logged out...  "))
    return redirect('login_user')
