from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.

class TagModel(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name

class ProductModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='product_img', default='PRODUCT.png', validators=[FileExtensionValidator(['png', 'jpg'])])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tag = models.ManyToManyField(TagModel)
    
    def __str__(self) -> str:
        return self.title


