from django.contrib.auth.models import Group

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def signin(request, page_name, redirect_link = "", group_name = None):
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
                if redirect_link.endswith(".html"):
                    return render(request, redirect_link, {"name": username})
                else:
                    return redirect(redirect_link)
            else:
                context["login_error"] = f"You dont have permission to login as {group_name}"
        else:
            context["login_error"] = "Bad Credentials!!"
            # messages.error(request, "Bad Credentials!!")
            # return redirect('home')

    return render(request, page_name, context)
