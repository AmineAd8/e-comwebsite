from django.shortcuts import render, redirect
from .forms import ProductForm

# Create your views here.
def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('buyer-index')
        else:
            print('form is not valid')
    else:
        form = ProductForm()

    context = {
        "form": form,
        
    }
    return render(request, "seller/product_form.html", context)
