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

@login_required
def add_to_cart(request, pk):
    cart = CartModel.objects.get(user=request.user)
    cart.add_to_cart(pk)
    return redirect('product_detail', pk)

@login_required
def remove_from_cart(request, pk):
    cart = CartModel.objects.get(user=request.user)
    cart.remove_from_cart(pk)
    return redirect('user_cart')

@login_required
def user_cart(request):
    cart = CartModel.objects.get(user=request.user)
    quantity = Quantity.objects.all()
    # count the total price
    price = cart.total_price()
    
    context = {
        'cart': cart,
        'price': price,
        'quantity': quantity,
    }
    return render(request, 'buyer/cart.html', context)

@login_required
def update_quantity(request, product_id):
    if request.method == 'POST':
        product = ProductModel.objects.get(pk=product_id)
        form = QuantityForm(request.POST)
        if form.is_valid():
            quantity_value = form.cleaned_data['quantity']
            # Assuming you have a user associated with the quantity
            user = request.user
            # Create or update the quantity for the user and product
            quantity, created = Quantity.objects.get_or_create(user=user, product=product)
            quantity.quantity = quantity_value
            quantity.save()
            # Redirect back to the cart page or wherever appropriate
            return redirect('user_cart')
    else:
        
        return redirect('error_page')

@login_required
def checkout(request):
    if request.method == 'POST':
        shipping_form = ShippingForm(request.POST)
        if shipping_form.is_valid():
            # save the shipping information
            instance = shipping_form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('order', instance.id)
    else:
        shipping_form = ShippingForm()

    context = {
        'sh_f' : shipping_form,
    }
    return render(request, 'order/checkout.html', context)


@login_required   
def order(request, pk):
    shipping_infomation = ShippingInformation.objects.get(id=pk)
    quantity = Quantity.objects.all()
    cart = CartModel.objects.get(user=request.user)
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            # save the Order
            instance = order_form.save(commit=False)
            instance.user = request.user
            instance.shipping = shipping_infomation
            instance.total_price = cart.total_price()
            instance.save()
            for i in cart.product.all():
                instance.add_items(i.id)
                cart.remove_from_cart(i.id)
            return redirect('order_complete')
    else:
        order_form = OrderForm()
    context = {
        'order': order_form,
        'shipping_info': shipping_infomation,
        'quantity': quantity,
    }
    return render(request, 'order/order.html', context)

@login_required
def order_complete(request):
   
    return render(request, 'order/order_complete.html')


