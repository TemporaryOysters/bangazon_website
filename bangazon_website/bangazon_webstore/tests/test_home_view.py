from django.test import TestCase
from django.urls import reverse
import sys
sys.path.append("../")
from bangazon_webstore.views import home_view

class TestOrderCanBeCompleted(TestCase):

    def setUp(self):

    def test_can_query_product_types(self):
        pass

    def test_can_get_last_5_added_products_for_each_type(self):
        pass

    def test_clicking_on_product_redirects_to_product_detail_view(self):
        pass

if __name__ == '__main__':
     main()