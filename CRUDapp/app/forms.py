from django.forms import ModelForm, widgets
from .models import *;
from django import forms

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'customer_name' :  forms.TextInput(attrs= {'class': 'form-control text-center'}),
        }

class CustomerForm(ModelForm):
    class Meta:
        model = Customer;
        fields = '__all__';

class ProductForm(ModelForm):
    class Meta: 
        model = Product;
        fields = '__all__' 
    