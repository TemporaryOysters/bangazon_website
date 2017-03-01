from django.contrib.auth.models import User, Group
from django.views import generic
import sys
sys.path.append("../")
from bangazon_webstore.models import ProductType, Product
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login, authenticate
from bangazon_webstore import models


class ProductDetailView(TemplateView):
    template_name = "bangazon_webstore/product_detail.html"
    model = models.Product

def get_product_detail(request):
    product_detail_view = Product.objects.all()
    return render(request, 'bangazon_webstore/product_detail_view.html', {'product': product_detail_view})

# def add_product_to_order(request, pk):
#     product = models.Product.objects.get(id = pk)


#     try:
#         order_pk = models.Order.objects.get(customer = request.user.id, active = 1)
#         new_order = models.Order.objects.get(id = order_pk.id)
#     except:
#         customer = models.Customer.objects.get(user = request.user)
#         new_order = models.Order.objects.create(active = 1, customer = customer, payment_type = None)
#         new_order.save()

#     new_order.products.add(product)

#     return HttpResponseRedirect(redirect_to='/products')   