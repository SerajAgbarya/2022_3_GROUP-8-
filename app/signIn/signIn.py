from pyexpat.errors import messages

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def signin(request, page_name, home_page):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, home_page, {"name": username})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')

    return render(request, page_name)
