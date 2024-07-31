from cProfile import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ProfileModel, Quantity


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fields in ['username', 'email', 'password1', 'password2']:
            self.fields[fields].help_text = None

class UserUpdate(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fields in ['username', 'email']:
            self.fields[fields].help_text = None 

class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['image']

class QuantityForm(forms.ModelForm):
    class Meta:
        model = Quantity
        fields = ['quantity']
    

