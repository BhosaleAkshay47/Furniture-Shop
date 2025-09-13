from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
      model = User
      fields = ['username', 'email', 'password1', 'password2']

class CustomerProfileForm(forms.ModelForm):
  class Meta:
    model = Customer
    fields = ['name','locality','city','state','zipcode']
    widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'zipcode': forms.NumberInput(attrs={'class': 'form-control'}),
        }