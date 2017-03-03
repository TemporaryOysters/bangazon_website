from django.conf.urls import url, include
import sys
# sys.path.append("../")
from django.contrib import admin
from .views import customer_view, product_detail_view, product_view, bangazon_order_view
from .views.customer_view import RegisterViewSet, LoginViewSet
from .views.product_view import ProductViewSet


app_name = 'bangazon_webstore'

urlpatterns = [
    url(r'^register/', RegisterViewSet.as_view(), name='register'),
    url(r'^register_customer/', customer_view.register_customer, name='register_customer'),
    url(r'^login/', LoginViewSet.as_view(), name='login'),
    url(r'^login_customer/', customer_view.login_customer, name='login_customer'),
    url(r'^logout/', customer_view.logout_customer, name='logout'),
    url(r'^productdetail/', product_detail_view.get_product_detail, name='productdetail'),
    url(r'^products/', product_view.get_products, name='products'),
    url(r'^products/', product_view.get_products, name='products'),
    url(r'^order/', customer_view.logout_customer, name='order'),
    url(r'^account/', customer_view.logout_customer, name='account'),
    url(r'^cart/', bangazon_order_view.get_products_in_cart, name='cart'),
]
