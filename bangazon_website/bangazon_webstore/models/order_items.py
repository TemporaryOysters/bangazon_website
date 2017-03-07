from django.db import models
from . import bangazon_order_model, product_model


class OrderItems(models.Model):
    product = models.ForeignKey(product_model.Product, on_delete=models.CASCADE)
    order = models.ForeignKey(bangazon_order_model.BangazonOrder, on_delete=models.CASCADE)
