from django.test import TestCase
import sys
sys.path.append("../")
from bangazon_webstore.models import product_model

class TestProduct(TestCase):
    ''' 
    TestProduct tests the Product: model, serializer, & view to guarantee are code is doing what is expected.

    method list:
    -SetUpClass
    -test_product_model_can_be_created_with_correct_fields
    -test_product_model_can_be_created_with_correct_fields

    Argument List:
    -TestCase: This argument 
        
    Author: Joey Kirby, TempOysters
    '''

    @classmethod
    def setUp(self):
        self.kickball = product_model.Product(name="kickball", description="Round Ball", price=5)
        # seller="Joey", product_category="Toys"
        self.kickball.save()

    def test_product_model_can_be_created_with_correct_fields(self):
        self.assertIsInstance(self.kickball, product_model.Product)

        self.assertEqual(self.kickball.name, "kickball")
        self.assertEqual(self.kickball.description, "Round Ball")
        self.assertEqual(self.kickball.price, 5)
        # self.assertEqual(kickball.seller, "Joey")
        # self.assertEqual(kickball.name, "Toys")

if __name__ == '__main__':
    main()