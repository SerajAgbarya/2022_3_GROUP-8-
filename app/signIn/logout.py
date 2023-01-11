from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from app.constants import STUDENT_LOGIN_PAGE_PATH


@login_required(login_url=STUDENT_LOGIN_PAGE_PATH)
def student_logout(request):
    logout(request)
    return render(request, 'student/logout.html')
