import sqlite3
from django.db import models
from . import customer_model, product_type_model


class Product(models.Model):
    ''' 
    Product Class contains the essential fields and behaviors of the data stored in a product.

    Method List:
    -get_product_name
    -get_description
    -get_price
    -get_quantity
    -purchase_productitemQty):
    -get_purchased
    -get_seller
    -get_product_type

    Argument List:
    -models.Model: This argument allows the class to access field types.
        
    Author: Joey Kirby, TempOysters
    '''
    name = models.CharField(max_length=75)
    description = models.TextField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    quantity = models.IntegerField(default=1)
    seller = models.ForeignKey(customer_model.Customer)
    product_type = models.ForeignKey(product_type_model.ProductType)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.product_type)

    def get_product_name(self):
        return self.name

    def get_description(self):
        return self.description

    def set_description(self, new_description):
        self.description = new_description
        return new_description

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def purchase_product(self, itemQty):
        if itemQty > self.quantity:
            print("We don't have that kind of quantity for {}(s). Only {} available.".format(self.name, self.quantity))
        else:
            self.quantity = self.quantity - itemQty
            return self.quantity

    def seller_set_quantity(self, new_quantity):
        self.quantity = new_quantity
        return self.quantity

    def get_purchased(self):
        return self.purchased

    def get_seller(self):
        return self.seller

    def get_product_type(self):
        return self.product_type

