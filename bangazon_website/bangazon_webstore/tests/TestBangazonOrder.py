from django.test import TestCase
import sys
sys.path.append("../")
from bangazon_webstore.models import bangazon_order_model


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
        visa = PaymentType.objects.create(
            """
            card_number="1234123412341234",
            card_type="Visa", cvv="123",
            expiration_date="2018-01-01",
            name_on_card="Bada Bing"
            """)

        joey = Customer.objects.create(
            """
            name="Joey L",
            address="1234 Wrong way", city="Nashville",
            state="tennessee", postal_code="12345",
            payment_type=1
            """)

        joeys_order = BangazonOrder.objects.create(
            """
            customerId = 1
            payment_typeId = 1
            order_is_complete = 0
            """)

    def test_order_contains_all_necessary_info(self):
        """
        Tests that order is created
        with correct attributes
        and has been assigned to the logged in user (customer).
        """
        self.assertEqual(joeys_order[1], 1)
        self.assertEqual(joeys_order[2], 1)
        self.assertEqual(joeys_order[3], 0)

if __name__ == '__main__':
     main()