from django import forms
from users.models import CartModel

class CartForm(forms.ModelForm):
    class Meta:
        model = CartModel
        fields = ['product']