from django.db import models

class ProductType(models.Model):
    """
    Stores a single product type, "label_name"
    author: Richie Van Sickle
    """
    label_name = models.CharField(max_length=55)

    def get_product_type_label(self):
        """
        Returns the label_name
        author: Richie Van Sickle
        """
        return self.label_name 

    def get_five_recent_products(self):
        print("WHAT IS SELF?!? WHO AM I!?!?", self.label_name)
        return self.order_by('-pub_date')[:5]