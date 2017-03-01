from django.conf.urls import url, include
import sys
# sys.path.append("../")
from django.contrib import admin
from .views import customer_view, product_view
from .views.customer_view import RegisterViewSet, LoginViewSet
from .views.product_view import ProductViewSet


app_name = 'bangazon_webstore'

urlpatterns = [
    url(r'^register/', RegisterViewSet.as_view(), name='register'),
    url(r'^register_customer/', customer_view.register_customer, name='register_customer'),
    url(r'^login/', LoginViewSet.as_view(), name='login'),
    url(r'^login_customer/', customer_view.login_customer, name='login_customer'),
    url(r'^logout/', customer_view.logout_customer, name='logout'),
    url(r'^products/', product_view.get_products, name='products'),
    url(r'^products/', product_view.get_products, name='products'),
    url(r'^productdetail/', customer_view.logout_customer, name='productdetail'),
    url(r'^order/', customer_view.logout_customer, name='order'),
    url(r'^account/', customer_view.logout_customer, name='account'),
    url(r'^cart/', customer_view.logout_customer, name='cart'),
]
