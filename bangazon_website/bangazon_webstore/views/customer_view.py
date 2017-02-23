from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect
import sys
sys.path.append("../")
from bangazon_webstore.models import customer


class RegisterViewSet(TemplateView):

    template_name = "bangazon_webstore/register.html"

def register_customer(request):
    data = request.POST
    user = User.objects.create_user(
        email = data['email'],
        password = data['password'],
        )
    customer = Customer.objects.create(
        first_name = data['first_name'],
        last_name = data['last_name'],
        address = data['address'],
        city = data['city'],
        state_province = data['state_province'],
        country = data['country'],
        postal_code = data['postal_code'],
        user = user
    )
    return login_customer(request)

class LoginViewSet(TemplateView):

    template_name = "bangazon_webstore/login.html"

def login_customer(request):
    data = request.POST
    email = data['email']
    password = data['password']
    user = authenticate(
        username = email,
        password = password
    )
    if user is not None:
        login(request = request, user = user)
    else:
        return HttpResponseRedirect(redirect_to='/')
    return HttpResponseRedirect(redirect_to='/success')



def logout_customer(request):
    logout(request)
    return HttpResponseRedirect(redirect_to='/')