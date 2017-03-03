from django.shortcuts import render
from django.http import HttpResponseRedirect
from bangazon_webstore.models.product_model import Product
from bangazon_webstore.forms import SellProductForm

def create_a_product(request):
    print("THIS IS REQUEST:",request.user.id)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SellProductForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            post = form.save(commit=False)
            post.seller_id = request.user.id


            post.save()
            print("GOT TO SAVE")
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(redirect_to='/webstore/products/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SellProductForm()

    return render(request, 'bangazon_webstore/create_product.html', {'form': form})