from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='buyer-index'),
    path('product_detail/<int:pk>/', views.product_detail, name='product_detail'),
    path('category/<int:pk>/', views.category, name='category'),
]