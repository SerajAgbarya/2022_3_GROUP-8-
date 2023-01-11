from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from app.constants import STUDENT_LOGIN_PAGE_PATH
from app.models import ScholarshipRequest


@login_required(login_url=STUDENT_LOGIN_PAGE_PATH)
def submit_scholarship_reqeust(request):
    current_user = request.user
    if request.method == 'POST':
        form_data = request.POST

        # Create a new scholarship request object
        scholar_ship_request = ScholarshipRequest(
            degree_year=form_data['degree_year'],
            age=form_data['age'],
            financial_situation=form_data['financial_situation'],
            parent_work=form_data['parent_work'],
            special_needs=form_data['special_needs'],
            tenant=form_data['tenant'],
            volunteer=form_data['volunteer']
        )
        scholar_ship_request.user_id = current_user
        scholar_ship_request.save()
        messages.success(request, 'Your request has been received successfully')
        return redirect('../../')
    else:
        return scholarship_form(request)


@login_required(login_url=STUDENT_LOGIN_PAGE_PATH)
def scholarship_form(request):
    degree_year_choices = [(i, str(i)) for i in range(1, 5)]
    financial_situation_choices = [('bad', 'Bad'), ('mid', 'Mid'), ('good', 'Good')]
    yes_no_choices = [('yes', 'Yes'), ('no', 'No')]
    return render(request, 'student/scholarship-form.html', {
        'DEGREE_YEAR_CHOICES': degree_year_choices,
        'FINANCIAL_SITUATION_CHOICES': financial_situation_choices,
        'YES_NO_CHOICES': yes_no_choices,
    })


@login_required(login_url=STUDENT_LOGIN_PAGE_PATH)
def scholarship_view(request):
    current_user = request.user
    print('hi')
    requests = ScholarshipRequest.objects.filter(user_id=current_user)
    print('hi2')
    if len(requests) > 0:
        return render(request, 'student/scholarship-form-view.html', {'request': requests[0]})
    else:
        return render(request, 'student/scholarship-form-view.html', {'request': None})
    # TODO add info message that there is no opne requests . or att all we should not reach this form if no request eists
