from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.views import generic
from django.views.generic.base import TemplateView
import sqlite3
import sys
sys.path.append("../")
from bangazon_webstore.models import bangazon_order_model, paymenttypes
from collections import Counter

class BangazonOrderView(TemplateView):
    template_name = 'bangazon_webstore/templates/bangazon_order.html'

def get_products_in_cart(request):
    """
    Returns all Bangazon Orders in a list form
    Author: Mark Ellis
    """
    print('This is the request for user', request.user.id)
    # <--- This gets order related to logged in Customer
    active_order = bangazon_order_model.BangazonOrder.objects.get(customer__user = request.user)

    # <--- Gets all products on the active order
    products_on_order = active_order.product.all()
    print("This is the first product: ", products_on_order[0].name)

    # <--- var to hold total price
    total_price = 0
    for product in products_on_order:
        total_price += product.price

    # <--- Create and update array for products on order with name, quantity and total price/item
    product_array = []
    prod = Counter(products_on_order)
    for p, q in prod.items():
        product_array.append((p.name, q, p.price * q))

    # <--- payment method
    payment_types = paymenttypes.PaymentType.objects.filter(customer__user = request.user)

    return render(request, 'bangazon_webstore/bangazon_order.html', {"product": product_array, "total": total_price})
