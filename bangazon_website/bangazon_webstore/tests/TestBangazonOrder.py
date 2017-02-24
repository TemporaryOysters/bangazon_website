from django.test import TestCase
import sys
sys.path.append("../")
from bangazon_webstore.models import bangazon_order_model, paymenttypes, customer


class TestOrderCanBeCompleted(TestCase):
    """
    TestOrderCanBeCompleted tests that an order is complete with the following attributes.
    Method List:

    Argument List: unittest.TestCase gives the unittest model knowledge on what to test.
    Author: Mark Ellis, Temporary Oysters
    """

    def setUp(self):
        """
        Sets up a Test customer and payment type.
        """
        self.joey = customer.Customer(
            
            first_name = "Joey",
            last_name="L",
            address="1234 Wrong way", city="Nashville",
            state_province="tennessee",
            country="USA",
            postal_code="12345",
            user = 1
            )
        
        self.visa = paymenttypes.PaymentType(
            
            card_number="1234123412341234",
            card_type="Visa", cvv="123",
            expiration_date="2018-01-01",
            name_on_card="Bada Bing",
            customer = self.joey
            )

        self.joeys_order = bangazon_order_model.BangazonOrder(
            
            customer = self.joey,
            payment_type = self.visa,
            order_is_complete = 0
            )

    def test_order_contains_all_necessary_info(self):
        """
        Tests that order is created
        with correct attributes
        and has been assigned to the logged in user (customer).
        """
        self.assertEqual(self.joeys_order.customer, 1)
        self.assertEqual(self.joeys_order.payment_type, 1)
        self.assertEqual(self.joeys_order.order_is_complete, 0)

if __name__ == '__main__':
     main()