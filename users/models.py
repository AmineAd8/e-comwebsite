from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from seller.models import ProductModel
from django.core.validators import FileExtensionValidator


# Create your models here.
class Quantity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class CartModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(ProductModel)

    def __str__(self):
        return self.user.username + 'Cart'

    def add_to_cart(self, product_id):
        product = ProductModel.objects.get(id=product_id)
        quantity, created = Quantity.objects.get_or_create(user=self.user, product=product)
        quantity.quantity += 1
        if not created:
            quantity.save()
        self.product.add(product)
    
    def remove_from_cart(self, product_id):
        product = ProductModel.objects.get(id=product_id)
        quantity = Quantity.objects.get(user=self.user, product=product)
        self.product.remove(product)
        quantity.delete()

    def product_count(self):
        return self.product.count()
    
    def total_price(self, ):
        quantity = Quantity.objects.all()
        price = 0
        for i in self.product.all() :
            for j in quantity:
                if j.user == self.user and j.product == i:
                    price += int(i.price)*j.quantity

        return price




class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile', validators=[FileExtensionValidator(['png', 'jpg'])])

    def __str__(self):
        return self.user.username

    

