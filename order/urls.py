from django.urls import path, include
from . import views

urlpatterns = [
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('remove_item_from_cart/<int:pk>/', views.remove_from_cart, name='remove_form_cart'),
    path('cart/', views.user_cart, name='user_cart'),
    path('update_quantity/<int:product_id>/', views.update_quantity, name='update_quantity'),
    path('checkout/', views.checkout, name='checkout'),
    path('order/<int:pk>/', views.order, name='order'),
    path('payment_method/', views.payment_method, name='payment_method'),
    path('order_complete/', views.order_complete, name='order_complete'),
    path('paypal/', include("paypal.standard.ipn.urls")),
    path('payment_success/<int:pk>/', views.payment_success, name='payment_success'),
    path('payment_failed/', views.payment_cancelled, name='payment_failed')
]