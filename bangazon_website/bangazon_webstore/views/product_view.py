from django.contrib.auth.models import User, Group
from django.views import generic
from django.shortcuts import render
from django.views.generic.base import TemplateView
import sys
sys.path.append("../")
from bangazon_webstore.models import product_model, product_type_model


def get_products_types_and_count(request):
    product_type_queryset = product_type_model.ProductType.objects.all()
    p_queryset = []

    for pt in product_type_queryset:
        p = product_model.Product.objects.filter(product_type=pt.pk).order_by('pub_date')
        product_type_info = {
            'type_label_name': pt.label_name,
            'p_list': p.reverse()[:20],
            'count': p.count()
        }

        p_queryset.append(product_type_info)
        print("PLIST:", product_type_info['p_list'])

    print("PRODUCT QUERYSET", p_queryset)

    return render(request, 'bangazon_webstore/products.html', {
        'products_info': p_queryset
    })
