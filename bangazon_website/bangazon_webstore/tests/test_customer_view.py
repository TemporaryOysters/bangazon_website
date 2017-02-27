from django.test import TestCase
from django.urls import reverse
import sys
sys.path.append("../")
from bangazon_webstore.views import customer_view
from bangazon_webstore.models import customer_model


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
        self.joeyuser = customer_model.User(username = "j@j.com", password = "123456")

        self.joey = customer_model.Customer(first_name = 'Joey', last_name = 'Kirby', address = '787 East Silver St', city = 'Lebanon', state_province = 'Ohio', country = 'USA', postal_code = '35622', email = 'j@j.com', user = self.joeyuser)

    def test_customer_can_be_registered(self):
        """
        Tests that customers can be registered to the DB
        """
        response = self.client.post(reverse('bangazon_webstore:register_customer'), {'username':'j@j.com', 'password':'123456', 'first_name':'Joey', 'last_name':'Kirby', 'address':'787 East Silver St', 'city':'Lebanon', 'state_province':'Ohio', 'country':'USA', 'postal_code':'35622', 'email':'j@j.com'})
        pass

    def test_customer_can_logout(self):
        """
        Tests that customers can be registered to the DB
        """
        response = self.client.post(reverse('bangazon_webstore:register'), {'username':'j@j.com', 'password':'123456'})
        # print(response)
        pass

    def test_customer_can_login(self):
        """
        Tests that customers can be registered to the DB
        """
        response = self.client.post(reverse('bangazon_webstore:login_customer'), {'username':'j@j.com', 'password':'123456'})
        pass
        