from django.shortcuts import render, redirect

from app.models import ScholarshipRequest


def submit_scholarship_reqeust(request):
    current_user = request.user
    if request.method == 'POST':
        form_data = request.POST

        # Create a new scholarship request object
        request = ScholarshipRequest(
            degree_year=form_data['degree_year'],
            age=form_data['age'],
            financial_situation=form_data['financial_situation'],
            parent_work=form_data['parent_work'],
            special_needs=form_data['special_needs'],
            tenant=form_data['tenant'],
            volunteer=form_data['volunteer']
        )
        request.user_id = current_user
        request.save()
        return redirect('student/home/')
    else:
        return render(request, 'home-student.html')


def get_scholarship_reqeust(request):
    current_user = request.user
    requests = ScholarshipRequest.objects.filter(user_id=current_user)
    if len(requests) > 0:
        return render(request, 'student/scholarship-form-view.html', {'request': requests[0]})
    #TODO add info message that there is no opne requests . or att all we should not reach this form if no request eists