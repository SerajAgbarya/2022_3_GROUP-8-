from functools import wraps

from django.shortcuts import redirect

from app.constants import STUDENT_HOME_PAGE
from app.services.scholarship.scholarship_dao import have_approved_request


def approved_request_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        request_approved = have_approved_request(request.user)
        if not request_approved:
            return redirect(STUDENT_HOME_PAGE)
        return view_func(request, *args, **kwargs)

    return wrapper
