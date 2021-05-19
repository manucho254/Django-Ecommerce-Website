from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from products.models import Product

class Vendor_Register_Form(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2')

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'price', 'description', 'category', 'product_image')



        
