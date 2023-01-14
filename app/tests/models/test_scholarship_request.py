from django.test import TestCase

from app.constants import GOOD_SMALL, YES_SMALL, NO_SMALL
from app.models import ScholarshipRequest
from app.tests.test_utils import create_student


class ScholarshipRequestTest(TestCase):
    def setUp(self):
        self.user = create_student()
        self.scholarship_request = ScholarshipRequest.objects.create(
            user_id=self.user,
            degree_year=3,
            age=25,
            financial_situation=GOOD_SMALL,
            parent_work=YES_SMALL,
            special_needs=NO_SMALL,
            tenant=YES_SMALL,
            volunteer=NO_SMALL
        )

    def test_scholarship_request_fields(self):
        self.assertTrue(isinstance(self.scholarship_request, ScholarshipRequest))
        self.assertEqual(self.scholarship_request.user_id, self.user)
        self.assertEqual(self.scholarship_request.degree_year, 3)
        self.assertEqual(self.scholarship_request.age, 25)
        self.assertEqual(self.scholarship_request.financial_situation, GOOD_SMALL)
        self.assertEqual(self.scholarship_request.parent_work, YES_SMALL)
        self.assertEqual(self.scholarship_request.special_needs, NO_SMALL)
        self.assertEqual(self.scholarship_request.tenant, YES_SMALL)
        self.assertEqual(self.scholarship_request.volunteer, NO_SMALL)
        self.assertEqual(self.scholarship_request.status, ScholarshipRequest.PENDING)
        self.assertEqual(self.scholarship_request.points, 0)
