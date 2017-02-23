import sqlite3
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    # seller = models.ForeignKey(customer.Customer)
    # product_category = models.ForeignKey(product_category.ProductCategory)

    def get_product_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    def purchase_product(self, itemQty):
        if itemQty > self.quantity:
            print("We don't have that kind of quantity for {}. Only {} available".format(self.name, self.quantity))
        else:
            self.quantity = self.quantity - itemQty
            return self.quantity

    def seller_set_quantity(self, new_quantity):
        self.quantity = new_quantity
        return self.quantity

    def get_purchased(self):
        return self.purchased

    def get_seller(self):
        pass

    def get_product_category(self):
        pass
