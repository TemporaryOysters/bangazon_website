from django.test import TestCase
import sys
sys.path.append("../")
from bangazon_webstore.models import product_type_model

class TestProductType(TestCase):


    @classmethod 
    def setUp(self):
        """
        Sets up a product type, "food", so we are able to test that food
        is a product_type
        author: Richie Van Sickle
        """ 
        self.food = product_type_model.ProductType(label_name='food')


    def test_can_create_instance_of_product_type(self):
        """
        Tests to see if an instance of product type can be created
        author: Richie Van Sickle
        """
        self.assertIsInstance(self.food, product_type_model.ProductType) 

    def test_product_type_has_correct_attributes(self):
        """
        Tests that the attribute in product_type is corresponding with 
        the correct value associated with it
        author: Richie Van Sickle
        """
        self.assertEqual(self.food.get_product_type_label(), 'food')          
