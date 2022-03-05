 
from django.contrib.auth.models import User
from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('user', 'name','weight','price',)

        widgets = {
           
            'user': forms.TextInput(attrs={'class': 'form-control','value':'','id':'elder','type':'hidden'}),
             'name': forms.TextInput(attrs={'class': 'form-control'}),
             'weight': forms.TextInput(attrs={'class': 'form-control'}),
             'price': forms.TextInput(attrs={'class': 'form-control'}),


        }