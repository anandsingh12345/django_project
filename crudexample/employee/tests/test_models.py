from django.test import TestCase
from employee.models import Employee
from django.utils import timezone
import pytz


class TestModel(TestCase):

    def setUp(self):
        self.emp = Employee.objects.create(
            eid = 'E5006',
            designation = 'CSE',
            dateofjoining = timezone.now(),
            name = 'Shivam',
            address = 'Chennai 123',
            phonenumber = '123456',
            email = 's@gmail.com'
        )

    def test_model_based_on_eid(self):
        self.assertEquals(self.emp.eid,'E5006')