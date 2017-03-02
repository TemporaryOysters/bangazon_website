from django.db import models
from . import customer_model, paymenttypes

class BangazonOrder(models.Model):
    """
    Join table containing Products and Order

    Method List:
    -get_orders_containing_product
    -get_products_on_order

    Argument List:
    -models.Model Allows the class to access field types

    Author: Mark Ellis
    """
    customer = models.ForeignKey(customer_model.Customer, on_delete=models.CASCADE)
    payment_type = models.ForeignKey(paymenttypes.PaymentType, on_delete=models.CASCADE)
    order_is_complete = models.BooleanField()

    def set_order_is_complete(self):
        self.order_is_complete = 1
        return self.order_is_complete

    def get_order_is_complete(self):
        return self.order_is_complete