from django.test import TestCase
import sys
sys.path.append("../")
from bangazon_webstore.models import product_model

class TestProduct(TestCase):
    ''' 
    TestProduct tests the Product: model, serializer, & view to guarantee are code is doing what is expected.

    method list:
    -setUp
    -test_product_model_can_be_created_with_correct_fields
    -test_product_can_be_purchased
    -test_seller_can_set_new_quantity

    Argument List:
    -TestCase: unittest provides a base class, TestCase, which may be used to create new test cases.
        
    Author: Joey Kirby, TempOysters
    '''
    print("TestProduct: 3 tests")

    @classmethod
    def setUp(self):
        self.kickball = product_model.Product(name="kickball", description="Round Ball", price=5, quantity=3)
        # seller="Joey", product_category="Toys"
        self.kickball.save()

    def test_product_model_can_be_created_with_correct_fields(self):
        self.assertIsInstance(self.kickball, product_model.Product)
        self.assertEqual(self.kickball.get_product_name(), "kickball")
        self.assertEqual(self.kickball.get_description(), "Round Ball")
        self.assertEqual(self.kickball.get_price(), 5)
        self.assertEqual(self.kickball.get_quantity(), 3)
        # self.assertEqual(kickball.seller, "Joey")
        # self.assertEqual(kickball.name, "Toys")

    def test_product_can_be_purchased(self):
        self.kickball.purchase_product(1)
        self.assertEqual(self.kickball.get_quantity(), 2)

    def test_seller_can_set_new_quantity(self):
        self.assertEqual(self.kickball.seller_set_quantity(50), 50)

if __name__ == '__main__':
    main()