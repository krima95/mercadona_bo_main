from .models import Product, Promotion
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, LoginForm, AddProductForm, UpdateProductForm, PromotionForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .serializers import CategorySerializer, ProductSerializer, PromotionSerializer
from rest_framework import viewsets
    # generics

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    # Récupérez tous les produits triés par id
    products = Product.objects.all().order_by('id')

    # Nombre d'articles par page
    items_per_page = 10

    # Récupérez le numéro de page à partir de la requête, par défaut 1
    page = request.GET.get('page', 1)

    # Créez un objet Paginator avec les produits et le nombre d'articles par page
    paginator = Paginator(products, items_per_page)

    try:
        # Récupérez les produits pour la page demandée
        items_page = paginator.page(page)
    except PageNotAnInteger:
        # Si le paramètre de page n'est pas un entier, affichez la première page
        items_page = paginator.page(1)
    except EmptyPage:
        # Si la page est hors limites, affichez la dernière page
        items_page = paginator.page(paginator.num_pages)

    context = {
        'products': items_page,
    }

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


# Afficher un produit
@login_required(login_url='login')
def product(request, pk):

    all_products = Product.objects.get(id=pk)

    context = {'product': all_products}

    return render(request, 'products/view-product.html', context=context)


# Supprimer un produit
@login_required(login_url='login')
def delete_product(request, pk):

    product = Product.objects.get(id=pk)

    product.delete()

    messages.success(request, "Le produit a été supprimé avec succès")

    return redirect("products/dashboard")

# Ajouter une promotion
def promotion(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = PromotionForm(request.POST)
        if form.is_valid():
            promotion = form.save(commit=False)
            promotion.product = product
            promotion.save()

            # Effectuez le calcul du prix avant la remise ici
            initial_price = product.sale_price if product.sale_price is not None else product.price
            discount_percentage = promotion.discount_percentage
            new_price = initial_price - (initial_price * (discount_percentage / 100))

            # Mettez à jour le champ sale_price et le champ price_before_discount du produit et enregistrez-le
            product.sale_price = new_price
            product.price_before_discount = initial_price
            product.save()

            return redirect('dashboard')
    else:
        form = PromotionForm()

    return render(request, 'products/promotion.html', {'form': form, 'product': product})

"""
# API views
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
"""