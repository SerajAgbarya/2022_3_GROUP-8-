from django.test import TestCase

from app.models import PointsByYear, PointsByAge, PointsByFinancialSituation, PointsByParentWork, PointsBySpecialNeeds, \
    PointsByTenant


class ReferenceDataTest(TestCase):
    def setUp(self):
        self.points_by_year = PointsByYear.objects.create(degree_year=1, points=10)
        self.points_by_age = PointsByAge.objects.create(minAge=18, maxAge=22, points=5)
        self.points_by_financial_situation = PointsByFinancialSituation.objects.create(financial_situation='GOOD',
                                                                                       points=8)
        self.points_by_parent_work = PointsByParentWork.objects.create(parent_work='YES', points=3)
        self.points_by_special_needs = PointsBySpecialNeeds.objects.create(special_needs='NO', points=0)
        self.points_by_tenant = PointsByTenant.objects.create(tenant='YES', points=2)

    def test_points_by_year_creation(self):
        self.assertTrue(isinstance(self.points_by_year, PointsByYear))
        self.assertEqual(self.points_by_year.degree_year, 1)
        self.assertEqual(self.points_by_year.points, 10)

    def test_points_by_age_creation(self):
        self.assertTrue(isinstance(self.points_by_age, PointsByAge))
        self.assertEqual(self.points_by_age.minAge, 18)
        self.assertEqual(self.points_by_age.maxAge, 22)
        self.assertEqual(self.points_by_age.points, 5)

    def test_points_by_financial_situation_creation(self):
        self.assertTrue(isinstance(self.points_by_financial_situation, PointsByFinancialSituation))
        self.assertEqual(self.points_by_financial_situation.financial_situation, 'GOOD')
        self.assertEqual(self.points_by_financial_situation.points, 8)

    def test_points_by_parent_work_creation(self):
        self.assertTrue(isinstance(self.points_by_parent_work, PointsByParentWork))
        self.assertEqual(self.points_by_parent_work.parent_work, 'YES')
        self.assertEqual(self.points_by_parent_work.points, 3)

    def test_points_by_special_needs_creation(self):
        self.assertTrue(isinstance(self.points_by_special_needs, PointsBySpecialNeeds))
        self.assertEqual(self.points_by_special_needs.special_needs, 'NO')
        self.assertEqual(self.points_by_special_needs.points, 0)

    def test_points_by_tenant_creation(self):
        self.assertTrue(isinstance(self.points_by_tenant, PointsByTenant))
        self.assertEqual(self.points_by_tenant.tenant, 'YES')
        self.assertEqual(self.points_by_tenant.points, 2)
