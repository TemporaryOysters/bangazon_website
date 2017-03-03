from django.contrib.auth.models import User, Group
from django.views import generic
from django.shortcuts import render
from django.views.generic.base import TemplateView
import sys
sys.path.append("../")
from bangazon_webstore.models import product_model, product_type_model


class ProductViewSet(TemplateView):

    template_name = "bangazon_webstore/products.html"

def get_products(request):
    product_queryset = product_model.Product.objects.all()

    return render(request, 'bangazon_webstore/products.html', {'product':product_queryset})
