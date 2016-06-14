from django.test import TestCase
from django.shortcuts import resolve_url as r
from djexperience.crm.models import Customer, Occupation
from .data import CUSTOMER_DICT


class CustomerDetailGet(TestCase):

    def setUp(self):
        self.occupation = Occupation.objects.create(occupation='Vendedor')
        self.obj = Customer.objects.create(
            occupation=self.occupation,
            **CUSTOMER_DICT)
        self.resp = self.client.get(
            r('crm:customer_detail', slug='mike-smith'))

    def test_create(self):
        self.assertTrue(Customer.objects.exists())

    def test_get(self):
        ''' GET shuld return status 200 '''
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'crm/customer_detail.html')

    def test_html(self):
        contents = [
            (1, 'Editar'),
        ]

        for count, expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected, count)

    # def test_context(self):
    #     ''' Customer must be in context '''
    #     customer = self.resp.context['customer']
    #     self.assertIsInstance(customer, Customer)


class CustomerDetailNotFound(TestCase):

    def test_not_found(self):
        response = self.client.get(r('crm:customer_detail', slug='not-found'))
        self.assertEqual(404, response.status_code)
