from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from app.constants import STUDENT_LOGIN_PAGE_PATH
from app.models import VolunteerHours, Task


@login_required(login_url=STUDENT_LOGIN_PAGE_PATH)
def student_volunteer_page(request):
    user = request.user
    hours = VolunteerHours.objects.filter(user_id=user.id)
    tasks = Task.objects.filter(user_id=user.id)
    context = {'volunteer_hours_list': hours, 'tasks': tasks}
    return render(request, 'student/student_volunteer.html', context)


@login_required(login_url=STUDENT_LOGIN_PAGE_PATH)
def student_save_volunteer(request):
    if request.method == 'POST':
        print(request.POST)
        user = request.user
        date_string = request.POST['date']
        hours = request.POST['hours']
        task_id = request.POST['task']
        task = Task.objects.get(id=task_id)
        date = datetime.strptime(date_string, '%Y-%m-%d')
        task.completed_hours += int(hours)
        if task.status == Task.TO_DO:
            task.status = Task.IN_PROGRESS
        if task.completed_hours >= task.total_hours:
            task.status = Task.COMPLETED
        now = datetime.now()
        task.created_at = now
        task.updated_at = now
        task.save()
        VolunteerHours.objects.create(date=date, hours=hours, task_id=task, user_id=user)
        return redirect('../../volunteer/')
    else:
        return JsonResponse({'error': 'Invalid request method'})
