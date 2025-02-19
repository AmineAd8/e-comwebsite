from turtle import title
from django.db import models
from users.models import CartModel
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from seller.models import ProductModel
from users.models import Quantity
from django.utils import timezone

# Create your models here.
class OrderItemModel(models.Model):
    title = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_img', validators=[FileExtensionValidator(['png', 'jpg'])])
    
    def __str__(self):
        return self.title + '_' + str(self.id)

class ShippingInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    adress1 = models.CharField(max_length=50)
    adress2 = models.CharField(max_length=50, blank=True, null=True)
    zip_address = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username + '_' + 'Information' + '_' + str(self.id)

class OrderModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shipping = models.ForeignKey(ShippingInformation, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItemModel)
    total_price = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)

    def add_items(self, product_id):
        product = ProductModel.objects.get(id=product_id)
        quantity = Quantity.objects.get(user=self.user, product=product)
        item, created = OrderItemModel.objects.get_or_create(title=product.title, quantity=quantity.quantity, price=product.price, image=product.image)
        if not created:
            item.save()
        self.items.add(item)
        
    def __str__(self):
        return self.user.username + '_' + 'Order' + '_' + str(self.id)





