from django.contrib import messages
from django.shortcuts import render, redirect

from app.models import ScholarshipRequest


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
        return redirect('../../student/')
    else:
        return get_scholarship_reqeust(request)


def get_scholarship_reqeust(request):
    current_user = request.user
    print('hi')
    requests = ScholarshipRequest.objects.filter(user_id=current_user)
    print('hi2')
    if len(requests) > 0:
        return render(request, 'student/scholarship-form-view.html', {'request': requests[0]})
    else:
        return render(request, 'student/scholarship-form-view.html', {'request': None})
    #TODO add info message that there is no opne requests . or att all we should not reach this form if no request eists