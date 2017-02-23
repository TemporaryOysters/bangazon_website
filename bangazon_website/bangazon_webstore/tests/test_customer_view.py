from django.test import TestCase
from django.urls import reverse
import sys
sys.path.append("../")
from bangazon_webstore.views import customer_view
from bangazon_webstore.models import customer


class TestCustomerView(TestCase):

    """
    TestCustomerView tests the customer can be registered and can logout.
    Method List:   
    -test_customer_be_registered
    -test_customer_can_login
    -test_customer_can_logout
    Argument List:  unittest.TestCase gives the unittest model knowledge on what to test.
    Author: Trent Hand, Temporary Oysters
    """ 

    @classmethod
    def setUp(self):
        """
        Sets up a Test User, "Joey", so we can TEST if our code is behaving as expected.
        """
        self.joeyuser = customer.User(email = "j@j.com", password = "1234")

        self.joey = customer.Customer(first_name = 'Joey', last_name = 'Kirby', address = '787 East Silver St', city = 'Lebanon', state_province = 'Ohio', postal_code = '35622', user = self.joeyuser)

    def test_customer_can_be_registered(self):
        """
        Tests that customers can be registered to the DB
        """
        response = self.client.post(reverse('bangazon_webstore:register'), {'email':'j@j.com', 'password':'1234'})
        # print(response)
        pass

    def test_customer_can_login(self):
        """
        Tests that customers can be registered to the DB
        """
        response = self.client.post(reverse('bangazon_webstore:login_customer'), {'email':'j@j.com', 'password':'1234'})
        # self.assertContains(response, )
        pass

    def test_customer_can_logout(self):
        """
        Tests that customers can be registered to the DB
        """
        response = self.client.post(reverse('bangazon_webstore:register'), {'email':'j@j.com', 'password':'1234'})
        # print(response)
        pass