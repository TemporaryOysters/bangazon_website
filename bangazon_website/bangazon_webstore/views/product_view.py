from django.contrib.auth.models import User, Group
from django.views import generic
import sys
sys.path.append("../")
from bangazon_webstore.models import product_model


class ProductViewSet(generic.ListView):
    context = product_model.Product.objects.all()