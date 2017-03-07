from django.contrib.auth.models import User, Group
from django.views import generic
import sys
sys.path.append("../")
from bangazon_webstore.models import ProductType, Product, BangazonOrder, Customer, OrderItems
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login, authenticate
from bangazon_webstore import models


class ProductDetailView(DetailView):
    model = Product

def get_product_detail(request):
    product_detail_view = Product.objects.filter(id=id)
    return render(request, 'bangazon_webstore/product_detail.html', {'product': product_detail_view})

def add_product_to_order(request, pk):
    print("REQUEST IS HERE:::::::::: ", request)
    product = Product.objects.get(id = pk)


    try:
        order_pk = BangazonOrder.objects.get(customer = request.user.id)
        new_order = BangazonOrder.objects.get(id = order_pk.id, order_is_complete = False)
    except:
        customer = Customer.objects.get(user = request.user)
        new_order = BangazonOrder.objects.create(order_is_complete = False, customer = customer, payment_type = None)
        new_order.save()

    orderitem = models.OrderItems(product=product, order=new_order)
    orderitem.save()

    return HttpResponseRedirect(redirect_to='/webstore/products/')
