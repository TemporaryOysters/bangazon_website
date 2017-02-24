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

