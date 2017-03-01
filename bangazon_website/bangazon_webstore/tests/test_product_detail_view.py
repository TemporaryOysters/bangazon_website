from django.test import TestCase
from django.urls import reverse
import sys
sys.path.append("../")
from bangazon_webstore.views import product_detail_view
from bangazon_webstore.models import product_detail_view 


class TestProductDetailView(TestCase):

    def setUp(self):
        user_rvs = User.objects.create_user(
            email = "r@vs.com",
            password = "123456"
            )

        self.customer = customer_model.Customer(
            first_name = "Richie",
            last_name="Van Sickle",
            address="500 Interstate Blvd", city="Nashville",
            state_province="Tennessee",
            country="USA",
            postal_code="12345",
            user = self.user_rvs
            )

        

            