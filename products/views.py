from .models import Product
from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, AddProductForm, UpdateProductForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Page d'accueil
def home(request):

    return render(request, 'products/index.html')


# Formulaire créer un compte
def register(request):
    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Compte créé avec succès !")

            return redirect("login")

    context = {'form': form}

    return render(request, 'products/register.html', context=context)


# Formulaire se connecter

def login(request):
    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("dashboard")

    context = {'form': form}

    return render(request, 'products/login.html', context=context)


# Déconnexion
def user_logout(request):
    auth.logout(request)

    messages.success(request, "Vous êtes déconnecté !")

    return redirect("login")


# Tableau de bord
@login_required(login_url='login')
def dashboard(request):

    products = Product.objects.all()

    context = {'products': products}

    return render(request, 'products/dashboard.html', context=context)


# Ajouter un produit
@login_required(login_url='login')
def create_product(request):
    form = AddProductForm()

    if request.method == "POST":

        form = AddProductForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Le produit est ajouté avec succès")

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'products/create-product.html', context=context)


# Modifier un produit
@login_required(login_url='my-login')
def update_product(request, pk):

    product = Product.objects.get(id=pk)

    form = UpdateProductForm(instance=product)

    if request.method == 'POST':

        form = UpdateProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()

            messages.success(request, "Mise à jour du produit avec succès")

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'products/update-product.html', context=context)


# - Afficher un produit

@login_required(login_url='login')
def product(request, pk):

    all_products = Product.objects.get(id=pk)

    context = {'product': all_products}

    return render(request, 'products/templates/products/view-product.html', context=context)


# - Supprimer un produit

@login_required(login_url='login')
def delete_product(request, pk):

    product = Product.objects.get(id=pk)

    product.delete()

    messages.success(request, "Le produit est supprimé avec succès")

    return redirect("dashboard")

