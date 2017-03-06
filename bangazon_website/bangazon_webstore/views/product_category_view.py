from django.contrib.auth.models import User, Group
from django.views import generic
from django.shortcuts import render
from django.views.generic.base import TemplateView
import sys
sys.path.append("../")
from bangazon_webstore.models.product_model import Product
from bangazon_webstore.models.product_type_model import ProductType


def get_product_type_info(request, pk):
    product_type = ProductType.objects.filter(id=pk)
    products = Product.objects.filter(product_type=pk)
    return render(request, 'bangazon_webstore/product_category.html', {
        'product_list': products,
        'product_type': product_type[0]
            })

