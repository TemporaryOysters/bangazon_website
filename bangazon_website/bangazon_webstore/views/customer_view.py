from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
import sys
sys.path.append("../")
from bangazon_webstore.models import customer_model


class RegisterViewSet(TemplateView):

    template_name = "bangazon_webstore/register.html"

def register_customer(request):
    data = request.POST
    user = User.objects.create_user(
        username = data['username'],
        password = data['password'],
        )
    customer = customer_model.Customer.objects.create(
        first_name = data['first_name'],
        last_name = data['last_name'],
        address = data['address'],
        city = data['city'],
        state_province = data['state_province'],
        country = data['country'],
        postal_code = data['postal_code'],
        email = data['email'],
        user = user
    )
    return login_customer(request)

class LoginViewSet(TemplateView):

    template_name = "bangazon_webstore/login.html"

def login_customer(request):
    data = request.POST
    username = data["username"]
    password = data['password']
    user = authenticate(
        username = username,
        password = password
    )
    if user is not None:
        login(request = request, user = user)
        return HttpResponseRedirect(redirect_to='/webstore/products')
    else:
        return HttpResponseRedirect(redirect_to='/webstore/login')


def logout_customer(request):
    logout(request)
    return HttpResponseRedirect(redirect_to='/webstore/login')