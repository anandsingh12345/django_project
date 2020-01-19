from django.test import SimpleTestCase
from django.urls import reverse,resolve
from employee.views import emp

class TestUrls(SimpleTestCase):
    def test_list_url(self):
        url = reverse('emp')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,emp)