from django.contrib.auth.models import Group

from app import constants
from app.constants import NO, YES, BAD, MID, GOOD, BAD_SMALL, GOOD_SMALL, MID_SMALL, NO_SMALL, YES_SMALL
from app.models import PointsByYear, PointsByAge, PointsByFinancialSituation, PointsByParentWork, PointsBySpecialNeeds, \
    PointsByTenant


def create_group_if_not_exists(group_name):
    group = Group.objects.filter(name=group_name).first()
    if group is None:
        group = Group(name=group_name)
        group.save()
    else:
        print(f'Group with name:{group_name} already exists')


def populate_default_points_by_year():
    for year in range(1, 5):
        PointsByYear.objects.update_or_create(degree_year=year, points=6 - year)


def populate_default_points_by_age():
    PointsByAge.objects.update_or_create(minAge=18, maxAge=20, points=10)
    PointsByAge.objects.update_or_create(minAge=21, maxAge=25, points=5)
    PointsByAge.objects.update_or_create(minAge=26, maxAge=100, points=2)


def populate_default_points_by_financial_situation():
    PointsByFinancialSituation.objects.update_or_create(financial_situation=BAD_SMALL, points=10)
    PointsByFinancialSituation.objects.update_or_create(financial_situation=MID_SMALL, points=5)
    PointsByFinancialSituation.objects.update_or_create(financial_situation=GOOD_SMALL, points=1)


def populate_default_points_by_parent_work():
    PointsByParentWork.objects.update_or_create(parent_work=NO_SMALL, points=6)
    PointsByParentWork.objects.update_or_create(parent_work=YES_SMALL, points=2)


def populate_default_points_by_special_needs():
    PointsBySpecialNeeds.objects.update_or_create(special_needs=NO_SMALL, points=3)
    PointsBySpecialNeeds.objects.update_or_create(special_needs=YES_SMALL, points=10)


def populate_default_points_by_tenant():
    PointsByTenant.objects.update_or_create(tenant=NO_SMALL, points=2)
    PointsByTenant.objects.update_or_create(tenant=YES_SMALL, points=8)


create_group_if_not_exists(constants.STUDENT)
create_group_if_not_exists(constants.WORKER)
create_group_if_not_exists(constants.MANAGER)

populate_default_points_by_year()
populate_default_points_by_age()
populate_default_points_by_financial_situation()
populate_default_points_by_parent_work()
populate_default_points_by_special_needs()
populate_default_points_by_tenant()
