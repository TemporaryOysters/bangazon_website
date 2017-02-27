from django.contrib.auth.models import User, Group
from django.views import generic
from django.shortcuts import render
from django.views.generic.base import TemplateView
import sys
sys.path.append("../")
from bangazon_webstore.models import product_model


class ProductViewSet(TemplateView):
    # context = product_model.Product.objects.all()

    template_name = "bangazon_webstore/products.html"