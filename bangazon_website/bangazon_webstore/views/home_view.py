from django.contrib.auth.models import User, Group
from django.views import generic
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.db.models import Q
import sys
sys.path.append("../")
from bangazon_webstore.models import product_model, product_type_model


def get_products_and_types(request):
    product_type_queryset = product_type_model.ProductType.objects.all()
    product_queryset = []

    for pt in product_type_queryset:
        p = product_model.Product.objects.filter(product_type=pt.pk).order_by('pub_date').reverse()[:5]
        product_queryset.append(p)


    return render(request, 'bangazon_webstore/home.html', {
        'product':product_queryset,
        'producttype':product_type_queryset
    })
