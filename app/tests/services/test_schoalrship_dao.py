from django.test import TestCase

from app.models import ScholarshipRequest
from app.services.scholarship.scholarship_dao import get_scholarship_request, get_or_create_scholar_ship_request, \
    have_approved_request, update_scholarship_request_entity
from app.tests.test_utils import create_student, create_scholarship_request, create_worker, get_scholarship_request_form


class ScholarshipRequestTest(TestCase):
    def setUp(self):
        self.user = create_student()
        self.scholarship_request = create_scholarship_request(self.user)
        self.form_data = get_scholarship_request_form()
        self.scholarship_request2 = ScholarshipRequest.objects.create(
            user_id=self.user,
            degree_year=2021,
            age=21,
            financial_situation='Bad',
            parent_work='Unemployed',
            special_needs='Special',
            tenant='No',
        )

    def test_get_scholarship_request(self):
        sc = get_scholarship_request(self.user)
        self.assertEqual(sc, self.scholarship_request)

    def test_get_or_create_scholar_ship_request(self):
        sc = get_or_create_scholar_ship_request(self.user)
        self.assertEqual(sc, self.scholarship_request)

        sc = get_or_create_scholar_ship_request(self.user)
        self.assertEqual(sc.user_id.username, self.user.username)

    def test_have_approved_request(self):
        self.assertTrue(have_approved_request(self.user))
        self.assertFalse(have_approved_request(create_worker()))

    def test_create_scholarship_request_entity(self):
        update_scholarship_request_entity(self.user, self.form_data, self.scholarship_request2)

        self.assertEqual(self.scholarship_request2.degree_year, 2022)
        self.assertEqual(self.scholarship_request2.age, 22)
        self.assertEqual(self.scholarship_request2.financial_situation, 'Good')
        self.assertEqual(self.scholarship_request2.parent_work, 'Farmer')
        self.assertEqual(self.scholarship_request2.special_needs, 'None')
        self.assertEqual(self.scholarship_request2.tenant, 'Yes')
        self.assertEqual(self.scholarship_request2.user_id, self.user)

    def test_create_scholarship_request_entity_with_empty_form(self):
        try:
            update_scholarship_request_entity(self.user, {}, self.scholarship_request2)
        except ValueError as ex:
            self.assertEqual(str(ex), 'missing mandatory keys')

    def test_create_scholarship_request_entity_with_partial_form(self):
        try:
            update_scholarship_request_entity(self.user, {'degree_year': 1}, self.scholarship_request2)
        except ValueError as ex:
            self.assertEqual(str(ex), 'missing mandatory keys')
