from django.test import TestCase
import sys
sys.path.append("../")
from bangazon_webstore.models import product_model, product_type_model, customer_model

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
    print("TestProduct: 4 tests")

    @classmethod
    def setUp(self):
        self.toys = product_type_model.ProductType(label_name="Toys")
        self.barbaraUser = customer_model.User(email = "b@b.com", password = "4321")
        self.barbara = customer_model.Customer(first_name = 'Barbara', last_name = 'Scout', address = '120 18th Ave', city = 'Nashville', state_province = 'TN', postal_code = '45909', user = self.barbaraUser )
        self.kickball = product_model.Product(name="kickball", description="Round Ball", price=5, quantity=3, seller=self.barbara, product_type=self.toys)

    def test_product_model_can_be_created_with_correct_fields(self):
        self.assertIsInstance(self.kickball, product_model.Product)
        self.assertEqual(self.kickball.get_product_name(), "kickball")
        self.assertEqual(self.kickball.get_description(), "Round Ball")
        self.assertEqual(self.kickball.get_price(), 5)
        self.assertEqual(self.kickball.get_quantity(), 3)
        self.assertEqual(self.kickball.get_seller(), self.barbara)
        self.assertEqual(self.kickball.get_product_type(), self.toys)

    def test_product_can_be_purchased(self):
        self.kickball.purchase_product(100)
        self.kickball.purchase_product(1)
        self.assertEqual(self.kickball.get_quantity(), 2)

    def test_seller_can_set_new_quantity(self):
        self.assertEqual(self.kickball.seller_set_quantity(50), 50)

    def test_can_set_new_description_on_product(self):
        updated_kb_description = "It really is a round ball"

        self.kickball.set_description(updated_kb_description)
        self.assertEqual(self.kickball.get_description(), "It really is a round ball")

if __name__ == '__main__':
    main()