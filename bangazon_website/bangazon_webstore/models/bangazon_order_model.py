from django.db import models
from . import customer, paymenttypes

class BangazonOrder(models.Model):
    """
    Stores a Bangazon Order
    author: Mark Ellis
    """
    customer = models.ForeignKey(customer.Customer, on_delete=models.CASCADE)
    payment_type = models.ForeignKey(paymenttypes.PaymentType, on_delete=models.CASCADE)
    order_is_complete = models.CharField(max_length=1)

    def set_order_is_complete(self):
        self.order_is_complete = 1
        return self.order_is_complete

    def get_order_is_complete(self):
        return self.order_is_complete
