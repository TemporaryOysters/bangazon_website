from django.contrib.auth.models import User, Group
from django.views import generic
from django.shortcuts import render
from django.views.generic.base import TemplateView
import sys
sys.path.append("../")
from bangazon_webstore.models import product_model, product_type_model


def get_category_info(request):
    category_info = None

    return render(request, 'bangazon_webstore/product_category.html', {
    'products_info': category_info
})