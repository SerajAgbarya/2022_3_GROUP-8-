from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from app.constants import STUDENT_LOGIN_PAGE_PATH, YES_SMALL
from app.models import ScholarshipRequest, PointsByYear, PointsByAge, PointsByFinancialSituation, PointsByParentWork, \
    PointsBySpecialNeeds, PointsByTenant


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
        calculate_points(scholar_ship_request)
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


def get_points_by_year(degree_year):
    try:
        points = PointsByYear.objects.get(degree_year=degree_year).points
        return points
    except PointsByYear.DoesNotExist:
        return 0


def get_points_by_age(age):
    try:
        points_by_age = PointsByAge.objects.get(minAge__lte=age, maxAge__gte=age)
        return points_by_age.points
    except PointsByAge.DoesNotExist:
        return 0


def get_points_by_financial_situation(financial_situation):
    try:
        points = PointsByFinancialSituation.objects.get(financial_situation=financial_situation.lower()).points
        return points
    except PointsByFinancialSituation.DoesNotExist:
        return 0


def get_points_by_parent_work(parent_work):
    try:
        points = PointsByParentWork.objects.get(parent_work=parent_work.lower()).points
        return points
    except PointsByParentWork.DoesNotExist:
        return 0


def get_points_by_special_needs(special_needs):
    try:
        points = PointsBySpecialNeeds.objects.get(special_needs=special_needs.lower()).points
        return points
    except PointsBySpecialNeeds.DoesNotExist:
        return 0


def get_points_by_tenant(tenant):
    try:
        points = PointsByTenant.objects.get(tenant=tenant.lower()).points
        return points
    except PointsByTenant.DoesNotExist:
        return 0


def calculate_points(scholar_ship_request):
    points = 0
    if scholar_ship_request.volunteer.lower() == YES_SMALL:
        points += get_points_by_year(scholar_ship_request.degree_year)
        points += get_points_by_age(scholar_ship_request.age)
        points += get_points_by_financial_situation(scholar_ship_request.financial_situation)
        points += get_points_by_parent_work(scholar_ship_request.parent_work)
        points += get_points_by_special_needs(scholar_ship_request.special_needs)
        points += get_points_by_tenant(scholar_ship_request.tenant)
    scholar_ship_request.points = points
    scholar_ship_request.save()
