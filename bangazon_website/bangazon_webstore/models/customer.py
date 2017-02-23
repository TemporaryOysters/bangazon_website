import sqlite3
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    """
    Extends :model:`auth.User`
    author: Trent Hand
    """
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=240)
    address = models.CharField(max_length=240)
    city = models.CharField(max_length=55)
    state_province = models.CharField(max_length=55)
    country = models.CharField(max_length=55)
    postal_code = models.CharField(max_length=9)
    user = models.OneToOneField(User)


