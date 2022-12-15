from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth import authenticate, login, logout

def main(request):
    return render(request, 'index.html')

def manager_signin(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "home-manager.html", { "name" :username })
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')

    return render(request, 'manager-signin.html')
