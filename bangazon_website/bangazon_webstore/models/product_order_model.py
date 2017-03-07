from django.db import models
from . import customer_model, bangazon_order_model, product_model

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
    order = models.ForeignKey(bangazon_order_model.BangazonOrder, on_delete=models.CASCADE)
