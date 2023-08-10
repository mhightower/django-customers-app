from django.test import TestCase
from customers.models import CustomerModel
from django.urls import reverse
from customers.forms import CustomerForm

class CustomerTestCase(TestCase):
    def setUp(self):
        CustomerModel.objects.create(first_name="Foo", last_name="Bar", address="123 State St", city="Chicago", zip_code="60001", state="IL")

    def test_customer_first_name(self):
        """An example of a model unit test"""
        customer = CustomerModel.objects.get(pk=1)
        self.assertEqual(customer.first_name, 'Foo')
        self.assertEqual(customer.last_name, 'Bar')
        self.assertEqual(customer.address, '123 State St')
        self.assertEqual(customer.city, 'Chicago')
        self.assertEqual(customer.zip_code, '60001')
        self.assertEqual(customer.state, 'IL')
    
    def test_customer_list_view(self):
        """An example of a list view unit test"""
        url = reverse('index')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
    
    def test_customer_add_view(self):
        """An example of an add view unit test"""
        url = reverse('add_customer')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
