from django.contrib.auth.models import Group
from django.test import TestCase

from app.constants import BAD_SMALL, MID_SMALL, GOOD_SMALL, NO_SMALL, YES_SMALL, STUDENT, WORKER, MANAGER
from app.models import PointsByYear, PointsByAge, PointsByFinancialSituation, PointsByParentWork, PointsBySpecialNeeds, \
    PointsByTenant
from ...services.reference_data.reference_data import create_group_if_not_exists, populate_default_points_by_year, \
    populate_default_points_by_parent_work, populate_default_points_by_financial_situation, \
    populate_default_points_by_age, populate_default_points_by_special_needs, populate_default_points_by_tenant, \
    create_reference_data


class CreateReferenceDataTestCase(TestCase):

    def test_create_group_if_not_exists(self):
        create_group_if_not_exists(STUDENT)
        group = Group.objects.filter(name=STUDENT).first()
        self.assertIsNotNone(group)

        create_group_if_not_exists(STUDENT)
        group = Group.objects.filter(name=STUDENT).first()
        self.assertIsNotNone(group)

    def test_populate_default_points_by_year(self):
        populate_default_points_by_year()
        for year in range(1, 5):
            points_by_year = PointsByYear.objects.filter(degree_year=year).first()
            self.assertEqual(points_by_year.points, 6 - year)

    def test_populate_default_points_by_age(self):
        populate_default_points_by_age()
        points_by_age = PointsByAge.objects.filter(minAge=18, maxAge=20).first()
        self.assertEqual(points_by_age.points, 10)
        points_by_age = PointsByAge.objects.filter(minAge=21, maxAge=25).first()
        self.assertEqual(points_by_age.points, 5)
        points_by_age = PointsByAge.objects.filter(minAge=26, maxAge=100).first()
        self.assertEqual(points_by_age.points, 2)

    def test_populate_default_points_by_financial_situation(self):
        populate_default_points_by_financial_situation()
        points_by_financial_situation = PointsByFinancialSituation.objects.filter(financial_situation=BAD_SMALL).first()
        self.assertEqual(points_by_financial_situation.points, 10)
        points_by_financial_situation = PointsByFinancialSituation.objects.filter(financial_situation=MID_SMALL).first()
        self.assertEqual(points_by_financial_situation.points, 5)
        points_by_financial_situation = PointsByFinancialSituation.objects.filter(
            financial_situation=GOOD_SMALL).first()
        self.assertEqual(points_by_financial_situation.points, 1)

    def test_populate_default_points_by_parent_work(self):
        populate_default_points_by_parent_work()
        points_by_parent_work = PointsByParentWork.objects.filter(parent_work=NO_SMALL).first()
        self.assertEqual(points_by_parent_work.points, 6)
        points_by_parent_work = PointsByParentWork.objects.filter(parent_work=YES_SMALL).first()
        self.assertEqual(points_by_parent_work.points, 2)

    def test_populate_default_points_by_special_needs(self):
        populate_default_points_by_special_needs()
        points_by_special_needs = PointsBySpecialNeeds.objects.filter(special_needs=NO_SMALL).first()
        self.assertEqual(points_by_special_needs.points, 3)
        points_by_special_needs = PointsBySpecialNeeds.objects.filter(special_needs=YES_SMALL).first()
        self.assertEqual(points_by_special_needs.points, 10)

    def test_populate_default_points_by_tenant(self):
        populate_default_points_by_tenant()
        points_by_tenant = PointsByTenant.objects.filter(tenant=NO_SMALL).first()
        self.assertEqual(points_by_tenant.points, 2)
        points_by_tenant = PointsByTenant.objects.filter(tenant=YES_SMALL).first()
        self.assertEqual(points_by_tenant.points, 8)

    def test_create_reference_data(self):
        create_reference_data(None, None)
        group = Group.objects.filter(name=STUDENT).first()
        self.assertIsNotNone(group)
        group = Group.objects.filter(name=WORKER).first()
        self.assertIsNotNone(group)
        group = Group.objects.filter(name=MANAGER).first()
        self.assertIsNotNone(group)
        for year in range(1, 5):
            points_by_year = PointsByYear.objects.filter(degree_year=year).first()
            self.assertEqual(points_by_year.points, 6 - year)
        points_by_age = PointsByAge.objects.filter(minAge=18, maxAge=20).first()
        self.assertEqual(points_by_age.points, 10)
        points_by_age = PointsByAge.objects.filter(minAge=21, maxAge=25).first()
        self.assertEqual(points_by_age.points, 5)
        points_by_age = PointsByAge.objects.filter(minAge=26, maxAge=100).first()
        self.assertEqual(points_by_age.points, 2)
        points_by_financial_situation = PointsByFinancialSituation.objects.filter(financial_situation=BAD_SMALL).first()
        self.assertEqual(points_by_financial_situation.points, 10)
        points_by_financial_situation = PointsByFinancialSituation.objects.filter(financial_situation=MID_SMALL).first()
        self.assertEqual(points_by_financial_situation.points, 5)
        points_by_financial_situation = PointsByFinancialSituation.objects.filter(
            financial_situation=GOOD_SMALL).first()
        self.assertEqual(points_by_financial_situation.points, 1)

    def test_create_reference_data(self):
        create_reference_data(None, None)
        group = Group.objects.filter(name=STUDENT).first()
        self.assertIsNotNone(group)
        group = Group.objects.filter(name=WORKER).first()
        self.assertIsNotNone(group)
        group = Group.objects.filter(name=MANAGER).first()
        self.assertIsNotNone(group)
        for year in range(1, 5):
            points_by_year = PointsByYear.objects.filter(degree_year=year).first()
            self.assertEqual(points_by_year.points, 6 - year)
        points_by_age = PointsByAge.objects.filter(minAge=18, maxAge=20).first()
        self.assertEqual(points_by_age.points, 10)
        points_by_age = PointsByAge.objects.filter(minAge=21, maxAge=25).first()
        self.assertEqual(points_by_age.points, 5)
        points_by_age = PointsByAge.objects.filter(minAge=26, maxAge=100).first()
        self.assertEqual(points_by_age.points, 2)
        points_by_financial_situation = PointsByFinancialSituation.objects.filter(financial_situation=BAD_SMALL).first()
        self.assertEqual(points_by_financial_situation.points, 10)
        points_by_financial_situation = PointsByFinancialSituation.objects.filter(financial_situation=MID_SMALL).first()
        self.assertEqual(points_by_financial_situation.points, 5)
        points_by_financial_situation = PointsByFinancialSituation.objects.filter(
            financial_situation=GOOD_SMALL).first()
        self.assertEqual(points_by_financial_situation.points, 1)
        points_by_parent_work = PointsByParentWork.objects.filter(parent_work=NO_SMALL).first()
        self.assertEqual(points_by_parent_work.points, 6)
        points_by_parent_work = PointsByParentWork.objects.filter(parent_work=YES_SMALL).first()
        self.assertEqual(points_by_parent_work.points, 2)
        points_by_special_needs = PointsBySpecialNeeds.objects.filter(special_needs=NO_SMALL).first()
        self.assertEqual(points_by_special_needs.points, 3)
        points_by_special_needs = PointsBySpecialNeeds.objects.filter(special_needs=YES_SMALL).first()
        self.assertEqual(points_by_special_needs.points, 10)
        points_by_tenant = PointsByTenant.objects.filter(tenant=NO_SMALL).first()
        self.assertEqual(points_by_tenant.points, 2)
        points_by_tenant = PointsByTenant.objects.filter(tenant=YES_SMALL).first()
        self.assertEqual(points_by_tenant.points, 8)
