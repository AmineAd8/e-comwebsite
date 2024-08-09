from unicodedata import name
from django.shortcuts import render, redirect, get_object_or_404
from seller.models import ProductModel, TagModel
from .froms import CartForm
from users.models import CartModel, Quantity
from users.forms import QuantityForm
from order.models import ShippingInformation, OrderModel, OrderItemModel
from order.forms import ShippingForm, OrderForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    product = ProductModel.objects.all()
    interval = range(0,3)
    tag = TagModel.objects.all()
    context = {
        'products': product,
        'tags' : tag,
        'range': interval,
    }
    return render(request, 'buyer/index.html', context)

def category(request, pk):
    product = ProductModel.objects.all()
    category = TagModel.objects.get(id=pk)
    tag = TagModel.objects.all()
    context = {
        'products': product,
        'category' : category,
        'tags' : tag,
    }
    return render(request, 'buyer/category.html', context)



def product_detail(request, pk):
    product = ProductModel.objects.get(id=pk)
    quantity = Quantity.objects.all()
    tag = TagModel.objects.all() 
    context = {
        'product': product,
        'tags' : tag,
        'quantity': quantity,        
    }
    return render(request, 'buyer/product_detail.html', context)



