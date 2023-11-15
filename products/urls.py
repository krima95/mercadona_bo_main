from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import ProductViewSet, PromotionViewSet
from django.conf.urls.static import static
from django.conf import settings

# API
router = DefaultRouter()
router.register(r"products", ProductViewSet)
router.register(r"promotions", PromotionViewSet)

urlpatterns = [
    path("", views.home, name=""),  # Accueil
    path("register", views.register, name="register"),  # Créer un compte
    path("login", views.login, name="login"),  # Ecran de connexion
    path("user-logout", views.user_logout, name="logout"),  # Déconnexion
    # CRUD
    path("dashboard", views.dashboard, name="dashboard"),  # Tableau de bord
    path(
        "create_product", views.create_product, name="create_product"
    ),  # Ajouter un produit
    path(
        "create_category", views.create_category, name="create_category"
    ),  # Ajouter un produit
    path(
        "update-product/<int:pk>", views.update_product, name="update-product"
    ),  # Modifier produit
    path("product/<int:pk>", views.product, name="product"),  # Afficher produit
    path(
        "promotion/<int:product_id>", views.promotion, name="promotion"
    ),  # Appliquer une promotion
    path(
        "edit_promotion/<int:promotion_id>", views.edit_promotion, name="edit-promotion"
    ),  # Modifier une promotion
    path(
        "delete_promotion/<int:promotion_id>",
        views.delete_promotion,
        name="delete-promotion",
    ),
    # Supprimer une promotion
    path(
        "delete-product/<int:pk>", views.delete_product, name="delete-product"
    ),  # Supprimer produit
    # API
    path("api/products/", include(router.urls)),
    #  path("api/promotions/", include(router.urls)),
]
