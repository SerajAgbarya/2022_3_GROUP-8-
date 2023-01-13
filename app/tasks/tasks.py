from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from app.constants import STUDENT_LOGIN_PAGE_PATH
from app.decorator.approved_request_required_decorator import approved_request_required
from app.tasks.tasks_dao import get_tasks


@login_required(login_url=STUDENT_LOGIN_PAGE_PATH)
@approved_request_required
def student_task_page(request):
    user = request.user
    tasks = get_tasks(user)
    context = {'tasks': tasks}
    return render(request, 'student/student_task.html', context)
