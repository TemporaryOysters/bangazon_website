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

def get_bangazon_orders(request):
    """
    Returns all Bangazon Orders in a list form
    Author: Mark Ellis
    """
    if request.user.is_authenticated() && user.id == customer.user
        authenticated_customer = customer.id
    all_orders_queryset = bangazon_order_model.BangazonOrder.objects.filter(authenticated_customer)

# Create product order join table