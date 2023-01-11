from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

from app.constants import STUDENT_LOGIN_PAGE_PATH


@login_required(login_url=STUDENT_LOGIN_PAGE_PATH)
def edit_student_personal_info(request):
    myuser = request.user
    context = {}
    changed = False
    new_pass = myuser.password
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1 != pass2:
            context["error"] = "Passwords didn't matched!!"
        elif pass1 != '':
            new_pass = make_password(pass1)
        if myuser.first_name != fname or myuser.last_name != lname or new_pass != myuser.password:
            changed = True
        if not context and changed:
            myuser.first_name = fname
            myuser.last_name = lname
            if new_pass != myuser.password:
                myuser.password = new_pass
            myuser.save()
            messages.success(request, "Your personal info has been updated successfully!")
        return redirect('../../')

    return render(request, 'student/edit_user_info.html', context)
