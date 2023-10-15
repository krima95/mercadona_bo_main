from django.forms import ModelForm
from django import forms
from .models import Product, Promotion
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput, ClearableFileInput
from django.core.exceptions import ValidationError
from datetime import timedelta
from django.utils import timezone
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django.utils.safestring import mark_safe


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
        fields = ('product_title', 'description', 'price', 'sale_price', 'image', 'category')

    def __init__(self, *args, **kwargs):
        super(UpdateProductForm, self).__init__(*args, **kwargs)
        product = self.instance

        if not 'sale_price' in self.fields and product.has_promotion():
            self.fields['sale_price'] = forms.DecimalField(
                label='Prix soldé',
                required=False,
                max_digits=10,
                decimal_places=2,
                initial=product.sale_price
            )

        # Personnalisation de l'affichage de l'image
        if product.image:
            image_html = f'<img src="{product.image.url}" width="100" />'
            self.fields['image'].help_text = mark_safe(image_html)
        else:
            self.fields['image'].help_text = 'Aucune image n\'est actuellement associée à ce produit.'

        self.fields['image'].widget = ClearableFileInput(attrs={'class': 'form-control'})


# Formulaire promotion
class PromotionForm(forms.ModelForm):
    class Meta:
        model = Promotion
        fields = ['start_date', 'end_date', 'discount_percentage']

# Formulaire filtres
class ProductFilterForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'product_title']

    def __init__(self, *args, **kwargs):
        super(ProductFilterForm, self).__init__(*args, **kwargs)
        self.fields['category'].required = False
        self.fields['product_title'].required = False

