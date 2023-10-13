from django.forms import ModelForm
from django import forms
from .models import Product, Promotion
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from django.core.exceptions import ValidationError
from datetime import timedelta
from django.utils import timezone


# Formulaire créer un user
class CreateUserForm(UserCreationForm):
    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']


# Formulaire connecter un user
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# Formulaire afficher les produits
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('product_title', 'description', 'price', 'sale_price', 'image', 'category')


# Formulaire ajouter un produit
class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_title', 'description', 'price', 'image', 'category')


# Formulaire modifier un produit
class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_title', 'description', 'price', 'image', 'category')

# Formulaire promotion
class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['start_date', 'end_date', 'discount_percentage']