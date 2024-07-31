from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='buyer-index'),
    path('product_detail/<int:pk>/', views.product_detail, name='product_detail'),
    path('category/<int:pk>/', views.category, name='category'),
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('remove_item_from_cart/<int:pk>/', views.remove_from_cart, name='remove_form_cart'),
    path('cart/', views.user_cart, name='user_cart'),
    path('update_quantity/<int:product_id>/', views.update_quantity, name='update_quantity'),
    path('checkout/', views.checkout, name='checkout'),
    path('order/<int:pk>/', views.order, name='order'),
    path('order_complete/', views.order_complete, name='order_complete'),
   
]