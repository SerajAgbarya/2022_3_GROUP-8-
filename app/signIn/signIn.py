from django.contrib.auth.models import Group

from django.contrib.auth import authenticate, login
from django.shortcuts import render


def signin(request, page_name, home_page, group_name):
    context = {}
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            group = Group.objects.get(name=group_name)
            if group in user.groups.all():
                login(request, user)
                # messages.success(request, "Logged In Sucessfully!!")
                return render(request, home_page, {"name": username})
            else:
                context["login_error"] = f"You dont have permission to login as {group_name}"
        else:
            context["login_error"] = "Bad Credentials!!"
            # messages.error(request, "Bad Credentials!!")
            # return redirect('home')

    return render(request, page_name, context)
