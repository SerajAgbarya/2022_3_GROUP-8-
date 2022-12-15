from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login








def home(request):
    return render(request, "authemnt/index.html")









def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name - lname

        myuser.save()

        messages.success(request, "You account has been succescfuly created.")

        return redirect('signin')

    return render(request, "authemnt/signup.html")








def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "authemnt/index.html", {'fname': fname})
        else:
            messages.error(request, "Bad Credntials!")
            return redirect('home')

    return render(request, "authemnt/signin.html")







def signout(request):
    pass