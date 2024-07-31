from django.contrib.auth.models import User
from .models import CartModel, ProfileModel
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_cart_and_profile(sender, instance, created, *args, **kwargs):
    if created:
        CartModel.objects.create(user=instance)
        ProfileModel.objects.create(user=instance)
    

        