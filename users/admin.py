from django.contrib import admin
from .models import CartModel, ProfileModel, Quantity

# Register your models here.
class QuantityAdmin(admin.ModelAdmin):
    list_display = ['user', 'product']

admin.site.register(CartModel)
admin.site.register(ProfileModel)
admin.site.register(Quantity, QuantityAdmin)




