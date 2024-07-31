from django.contrib import admin
from .models import ProductModel, TagModel

# Register your models here.
admin.site.register(ProductModel)
admin.site.register(TagModel)


