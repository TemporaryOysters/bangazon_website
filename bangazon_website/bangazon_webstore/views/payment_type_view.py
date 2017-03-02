from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from bangazon_webstore.forms import PaymentTypeForm


@login_required
def add_payment(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PaymentTypeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            post = form.save(commit=False)
            post.customer_id = request.user.id
            post.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/orders/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PaymentTypeForm()

    return render(request, 'bangazon_webstore/payment_type.html', {'form': form})


