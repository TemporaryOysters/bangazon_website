from django.conf.urls import url, include
import sys
# sys.path.append("../")
from django.contrib import admin
from .views import customer_view
from .views.customer_view import RegisterViewSet, LoginViewSet


app_name = 'bangazon_webstore'

urlpatterns = [
    url(r'^register/', RegisterViewSet.as_view(), name='register'),
    url(r'^login/', LoginViewSet.as_view(), name='login'),
    url(r'^login_customer/', customer_view.login_customer, name='login_customer'),
    url(r'^logout/', customer_view.logout_customer, name='logout'),
]
