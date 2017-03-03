from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.views import generic
from django.views.generic.base import TemplateView
import sqlite3
import sys
sys.path.append("../")
from bangazon_webstore.models import bangazon_order_model

class BangazonOrderView(TemplateView):
    template_name = 'bangazon_webstore/templates/bangazon_order.html'

def get_products_in_cart(request):
    """
    Returns all Bangazon Orders in a list form
    Author: Mark Ellis
    """
    print('This is the request for user', request.user.id)
    active_customer = bangazon_order_model.BangazonOrder.objects.filter(request.user.id)

    active_order = "not yet determined"

    users_payment_types = bangazon_paymenttypes.PaymentType.filter(customer="""
    the logged in customer""")

    products_on_order = bangazon_order_model.BangazonOrder.filter()




    # all_orders = bangazon_order_model.BangazonOrder.objects.filter()

    # def get_products_in_cart(self):
    # if customer is logged in 
    # get all products on order && all payment types
