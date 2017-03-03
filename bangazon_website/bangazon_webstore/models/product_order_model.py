from django.db import models
from . import customer_model, paymenttypes, product_model

class ProductOrder(models.Model):
    """
    Join table containing Products and Order

    Method List:

    -get_orders_containing_product
    -get_products_on_order

    Argument List:
    -models.Model Allows the class to access field types

    Author: Mark Ellis
    """
    product = models.ForeignKey(product_model.Product, on_delete=models.CASCADE)
    order = models.ForeignKey(paymenttypes.PaymentType, on_delete=models.CASCADE)
    order_is_complete = models.BooleanField()

    def get_orders_containing_product(self):
        self.order_is_complete = 1
        return self.order_is_complete

    def get_products_on_order(self):
        return self.order_is_complete