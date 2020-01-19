from django.test import TestCase,Client
from employee.models import Employee
from django.urls import reverse
import json

class TestViews(TestCase):

    def test_show_get(self):
        client = Client()

        response = client.get(reverse('show'))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'show.html')

    def test_edit_get(self):
        client = Client()

        response = client.get(reverse('edit'),args = ['edit/1'])

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'edit.html')    
