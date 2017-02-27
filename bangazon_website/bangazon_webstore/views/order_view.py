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
    with sqlite3.connect('../db.sqlite3') as conn:
        c = conn.cursor()
        command = """
        SELECT order
        FROM BangazonOrder
        """
        c.execute(command)
        all_orders = c.fetchall()
        return all_orders



    # all_orders = bangazon_order_model.BangazonOrder.objects.filter()

