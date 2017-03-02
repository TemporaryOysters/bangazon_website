from django.contrib.auth.models import User, Group
from django.views import generic
from django.shortcuts import render
from django.views.generic.base import TemplateView
import sys
sys.path.append("../")
from bangazon_webstore.models import product_model, product_type_model


def get_products_and_types(request):
    product_queryset = product_model.Product.objects.all()
    product_type_queryset = product_type_model.ProductType.objects.all()

    print("YOOOOOOO", product_type_queryset)

    return render(request, 'bangazon_webstore/home.html', {
        'product':product_queryset, 
        'producttype':product_type_queryset
    })