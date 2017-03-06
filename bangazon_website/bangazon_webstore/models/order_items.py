from django.db import models
from . import customer_model, paymenttypes, product_model


class OrderItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(BangazonOrder, on_delete=models.CASCADE)
