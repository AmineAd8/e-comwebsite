from django.contrib import admin
from .models import OrderItemModel, ShippingInformation, OrderModel
# Register your models here.
admin.site.register(OrderItemModel)
admin.site.register(ShippingInformation)
admin.site.register(OrderModel)
