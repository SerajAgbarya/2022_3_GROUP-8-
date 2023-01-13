from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from app.constants import STUDENT_LOGIN_PAGE_PATH, STUDENT_HOME_PAGE
from app.decorator.approved_request_required_decorator import approved_request_required
from app.scholarship.scholarship_dao import have_approved_request
from app.tasks.tasks_dao import get_tasks, get_task_by_id, progress_task
from app.volunteer.voulnteer_hours_dao import create_new_volunteer_hours, get_volunteer_hours


@login_required(login_url=STUDENT_LOGIN_PAGE_PATH)
def student_volunteer_page(request):
    request_approved = have_approved_request(request.user)
    if not request_approved:
        return redirect(STUDENT_HOME_PAGE)

    user = request.user
    hours = get_volunteer_hours(user)
    tasks = get_tasks(user)
    context = {'volunteer_hours_list': hours, 'tasks': tasks}
    return render(request, 'student/student_volunteer.html', context)


@login_required(login_url=STUDENT_LOGIN_PAGE_PATH)
@approved_request_required
def student_save_volunteer(request):
    if request.method == 'POST':
        user = request.user
        date_string = request.POST['date']
        hours = request.POST['hours']
        task_id = request.POST['task']
        task = get_task_by_id(task_id)
        progress_task(task, hours)
        date = datetime.strptime(date_string, '%Y-%m-%d')
        create_new_volunteer_hours(date, hours, task, user)
        return redirect('../../volunteer/')
    else:
        return JsonResponse({'error': 'Invalid request method'})
