from django.test import TestCase
import sys
sys.path.append("../")
from bangazon_webstore.models import customer_model
# Create your tests here.

class TestCustomer(TestCase):
    """
    TestCustomer tests the creation of a customer and it's methods.
    Method List:   
    -test_customer_acct_can_be_created
    -test_customer_has_correct_attributes
    Argument List:  unittest.TestCase gives the unittest model knowledge on what to test.
    Author: Trent Hand, Temporary Oysters
    """

    @classmethod
    def setUp(self):
        """
        Sets up a Test User, "Joey", so we can TEST if our code is behaving as expected.
        """
        self.joeyuser = customer_model.User(username = "j@j.com", password = "123456")

        self.joey = customer_model.Customer(first_name = 'Joey', last_name = 'Kirby', address = '787 East Silver St', city = 'Lebanon', state_province = 'Ohio', postal_code = '35622', email = 'j@j.com', user = self.joeyuser )
        
    def test_customer_acct_can_be_created(self):
        """
        Tests User, "Joey", has been created.
        """
        self.assertIsInstance(self.joey, customer_model.Customer)


    def test_customer_has_correct_attributes(self):
        """
        Tests that our users has created with the correct amount of attributes (6) & have value. 
        """
        self.assertEqual(self.joey.first_name, 'Joey')
        self.assertEqual(self.joey.last_name, 'Kirby')
        self.assertEqual(self.joey.address, '787 East Silver St')
        self.assertEqual(self.joey.city, 'Lebanon')
        self.assertEqual(self.joey.state_province, 'Ohio')
        self.assertEqual(self.joey.postal_code, '35622')
        self.assertEqual(self.joey.email, 'j@j.com')
        self.assertEqual(self.joey.user.username, 'j@j.com')
        self.assertEqual(self.joey.user.password, '123456')

    def test_customer_full_name(self):
        self.assertEqual(self.joey.get_full_name(), "Joey Kirby")


if __name__ == '__main__':
    unittest.main()

