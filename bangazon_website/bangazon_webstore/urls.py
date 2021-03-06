from django.conf.urls import url, include
import sys
# sys.path.append("../")
from django.contrib import admin
from .views import customer_view, product_detail_view, product_view, home_view, product_category_view, bangazon_order_view, payment_type_view
from .views.customer_view import RegisterViewSet, LoginViewSet
from .views.payment_type_view import add_payment
from .views.create_product_view import create_a_product


app_name = 'bangazon_webstore'

urlpatterns = [
    url(r'^register/', RegisterViewSet.as_view(), name='register'),
    url(r'^register_customer/', customer_view.register_customer, name='register_customer'),
    url(r'^login/', LoginViewSet.as_view(), name='login'),
    url(r'^login_customer/', customer_view.login_customer, name='login_customer'),
    url(r'^logout/', customer_view.logout_customer, name='logout'),
    url(r'^order/', customer_view.logout_customer, name='order'),
    url(r'^account/', customer_view.logout_customer, name='account'),
    url(r'^cart/', bangazon_order_view.get_products_in_cart, name='cart'),
    url(r'^addpayment/', payment_type_view.add_payment, name='addpayment'),
]

urlpatterns += [  url(r'^home/', home_view.get_products_and_types, name='home'),
]

urlpatterns += [
    url(r'^products/', product_view.get_products_types_and_count, name='products'),
    url(r'^producttype/(?P<pk>\d+)/', product_category_view.get_product_type_info, name='producttype'),
    url(r'^productdetail/(?P<pk>\d+)/', product_detail_view.ProductDetailView.as_view(), name='productdetail'),
    url(r'^add_product_to_order/(?P<pk>\d+)/', product_detail_view.add_product_to_order, name='add_product_to_order'),
    url(r'^addproduct/', create_a_product, name='addproduct'),
]
