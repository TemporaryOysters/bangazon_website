from django.shortcuts import render
from django.http import HttpResponseRedirect


from bangazon_webstore.forms import PaymentTypeForm

def add_payment(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PaymentTypeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/orders/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PaymentTypeForm()

    return render(request, 'bangazon_webstore/payment_type.html', {'form': form})