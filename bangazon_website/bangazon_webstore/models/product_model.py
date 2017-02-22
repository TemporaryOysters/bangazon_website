import sqlite3
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField()
    price = models.IntegerField()
    # seller = models.ForeignKey(customer.Customer)
    # product_category = models.ForeignKey(product_category.ProductCategory)
    # created_at = models.DateTimeField(auto_now_add=True, editable=False)