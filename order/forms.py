from django import forms
from .models import ShippingInformation, OrderModel

class ShippingForm(forms.ModelForm):
    class Meta:
        model = ShippingInformation
        fields = ['name', 'lastname', 'email', 'number', 'country', 'city', 'adress1', 'adress2', 'zip_address']

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = []
