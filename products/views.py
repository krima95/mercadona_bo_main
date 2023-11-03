from .models import Product, Promotion
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from .forms import (
    CreateUserForm,
    LoginForm,
    AddProductForm,
    UpdateProductForm,
    PromotionForm,
    ProductFilterForm,
    AddCategoryForm,
)
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .serializers import ProductSerializer, PromotionSerializer
from rest_framework import viewsets
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from decimal import Decimal


# Page d'accueil
def home(request):
    return render(request, "products/index.html")


# Formulaire créer un compte
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Compte créé avec succès !")

            return redirect("login")

    context = {"form": form}

    return render(request, "products/register.html", context=context)


# Formulaire se connecter
def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("dashboard")

    context = {"form": form}

    return render(request, "products/login.html", context=context)


# Déconnexion
def user_logout(request):
    auth.logout(request)

    messages.success(request, "Vous êtes déconnecté !")

    return redirect("login")


# Tableau de bord
@login_required(login_url="login")
def dashboard(request):
    filter_form = ProductFilterForm(request.GET)
    products = Product.objects.all().order_by("-creation_date")

    if filter_form.is_valid():
        category = filter_form.cleaned_data["category"]
        product_title = filter_form.cleaned_data["product_title"]

        if category:
            products = products.filter(category=category)

        if product_title:
            products = products.filter(product_title__icontains=product_title)

    context = {
        "products": products,
        "filter_form": filter_form,
    }

    return render(request, "products/dashboard.html", context=context)


# Ajouter un produit
@login_required(login_url="login")
def create_product(request):
    form = AddProductForm()

    if request.method == "POST":
        form = AddProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            messages.success(request, "Le produit est ajouté avec succès")

            return redirect("dashboard")

    context = {"form": form}

    return render(request, "products/create-product.html", context=context)


# Ajouter une catéguorie
@login_required(login_url="login")
def create_category(request):
    form = AddCategoryForm()

    if request.method == "POST":
        form = AddCategoryForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "La catéguorie est ajoutée avec succès")

            return redirect("dashboard")

    context = {"form": form}

    return render(request, "products/create-category.html", context=context)


# Modifier un produit
@login_required(login_url="my-login")
def update_product(request, pk):
    product = Product.objects.get(id=pk)

    form = UpdateProductForm(instance=product)

    if request.method == "POST":
        form = UpdateProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()

            messages.success(request, "Mise à jour du produit avec succès")

            return redirect("dashboard")

    context = {"form": form}

    return render(request, "products/update-product.html", context=context)


# Afficher un produit
@login_required(login_url="login")
def product(request, pk):
    all_products = Product.objects.get(id=pk)

    context = {"product": all_products}

    return render(request, "products/view-product.html", context=context)


## Supprimer un produit
@login_required(login_url="login")
def delete_product(request, pk):
    product = Product.objects.get(id=pk)

    product.delete()

    messages.success(request, "Le produit a été supprimé avec succès")

    return redirect("dashboard")


# Ajouter une promotion
@login_required(login_url="login")
def promotion(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        form = PromotionForm(request.POST)
        if form.is_valid():
            promotion = form.save(commit=False)
            promotion.product = product
            promotion.save()

            # Calcul du nouveau prix ici
            initial_price = (
                product.sale_price if product.sale_price is not None else product.price
            )
            discount_percentage = promotion.discount_percentage
            new_price = initial_price - (initial_price * (discount_percentage / 100))

            # Mettre à jour le champ sale_price et le champ price_before_discount du produit
            product.sale_price = new_price
            product.price_before_discount = initial_price
            product.save()

            return redirect("dashboard")
    else:
        form = PromotionForm()

    return render(
        request, "products/promotion.html", {"form": form, "product": product}
    )


# Modifier une promotion
def edit_promotion(request, promotion_id):
    promotion = get_object_or_404(Promotion, id=promotion_id)
    if request.method == "POST":
        form = PromotionForm(request.POST, instance=promotion)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = PromotionForm(instance=promotion)
    return render(
        request, "products/edit-promotion.html", {"form": form, "promotion": promotion}
    )


# Supprimer une promotion
def delete_promotion(request, promotion_id):
    promotion = get_object_or_404(Promotion, id=promotion_id)
    if request.method == "POST":
        promotion.delete()
        return redirect("dashboard")
    return render(request, "products/delete-promotion.html", {"promotion": promotion})


# API views
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
