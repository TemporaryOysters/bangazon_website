from django.db import models
# from . import customer, payment_type

class BangazonOrder(models.Model):
    """
    Stores a Bangazon Order
    author: Mark Ellis
    """
    # customerId = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # payment_typeId = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    customerId = 1
    payment_typeId = 1
