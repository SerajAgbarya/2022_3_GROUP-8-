from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from app.constants import STUDENT_LOGIN_PAGE_PATH, YES_SMALL, FINANCIAL_SITUATION_CHOICES, DEGREE_YEAR_CHOICES, \
    NO_YES_CHOICES, ON_SMALL, STUDENT_HOME_PAGE
from app.models import PointsByYear, PointsByAge, PointsByFinancialSituation, PointsByParentWork, \
    PointsBySpecialNeeds, PointsByTenant
from app.services.scholarship.scholarship_dao import get_scholarship_request, create_scholarship_request, \
    update_scholarship_request_entity


@login_required(login_url=STUDENT_LOGIN_PAGE_PATH)
def submit_scholarship_reqeust(request):
    current_user = request.user
    if request.method == 'POST':
        form_data = request.POST
        msg = 'updated'
        scholar_ship_request = get_scholarship_request(current_user)
        if scholar_ship_request is None:
            msg = 'received'
            f1 = 'volunteer' in form_data
            if f1 and form_data['volunteer'].lower() == ON_SMALL:
                scholar_ship_request = create_scholarship_request()
                scholar_ship_request.volunteer = YES_SMALL
            else:
                messages.error(request, f'Your request cant be accomplished, Volunteer is required!')
                return redirect(STUDENT_HOME_PAGE)

        update_scholarship_request_entity(current_user, form_data, scholar_ship_request)
        calculate_points(scholar_ship_request)
        scholar_ship_request.save()
        messages.success(request, f'Your request has been {msg} successfully')
        return redirect(STUDENT_HOME_PAGE)
    else:
        return scholarship_form_request_view(request)


@login_required(login_url=STUDENT_LOGIN_PAGE_PATH)
def scholarship_form_request_view(request):
    if get_scholarship_request(request.user) is None:
        return render(request, 'student/scholarship-form.html', {
            'DEGREE_YEAR_CHOICES': DEGREE_YEAR_CHOICES,
            'FINANCIAL_SITUATION_CHOICES': FINANCIAL_SITUATION_CHOICES,
            'YES_NO_CHOICES': NO_YES_CHOICES,
        })
    return scholarship_view_and_edit(request)


@login_required(login_url=STUDENT_LOGIN_PAGE_PATH)
def scholarship_view_and_edit(request):
    scholarship_request = get_scholarship_request(request.user)
    if scholarship_request is None:
        return scholarship_form_request_view(request)

    return render(request, 'student/scholarship-form-view.html', {'request': scholarship_request,
                                                                  'DEGREE_YEAR_CHOICES': DEGREE_YEAR_CHOICES,
                                                                  'FINANCIAL_SITUATION_CHOICES': FINANCIAL_SITUATION_CHOICES,
                                                                  'YES_NO_CHOICES': NO_YES_CHOICES})


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
