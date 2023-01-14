from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from app.constants import STUDENT_LOGIN_PAGE_PATH
from app.services.scholarship.scholarship_dao import get_scholarship_request, have_approved_request

STUDENT_HOME_PAGE_HTML = 'student/home-student.html'


@login_required(login_url=STUDENT_LOGIN_PAGE_PATH)
def student_home_page(request):
    have_request = get_scholarship_request(request.user) is not None
    request_approved = have_approved_request(request.user)
    return render(request, STUDENT_HOME_PAGE_HTML, {'have_request': have_request,
                                                    'request_approved': request_approved})
