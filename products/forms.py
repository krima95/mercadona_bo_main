from django.forms import ModelForm
from django import forms
from .models import Product
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput


# Créer un user
class CreateUserForm(UserCreationForm):
    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']


# Connecter un user
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# Afficher les produits
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('product_title', 'description', 'price', 'image', 'category')


# Ajouter un produit
class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_title', 'description', 'price', 'image', 'category')


# Modifier un produit
class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_title', 'description', 'price', 'image', 'category')






















