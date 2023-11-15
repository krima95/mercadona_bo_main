from datetime import datetime
from django.core.validators import MaxValueValidator
from django.db import models
from django.core.files.storage import FileSystemStorage


# Modèle Catégorie
class Category(models.Model):
    category_title = models.CharField(max_length=30, verbose_name="Catéguorie")

    class Meta:
        verbose_name = "Catéguorie"
        verbose_name_plural = "Catéguories"

    def __str__(self):
        return self.category_title


# Modèle Produit
class Product(models.Model):
    product_title = models.CharField(max_length=30, verbose_name="Nom du produit")
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix")
    sale_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Prix soldé",
        null=True,
        blank=True,
    )
    price_before_discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Prix initial",
        null=True,
        blank=True,
    )
    image = models.ImageField(
        blank=True,
        upload_to="images/",
        default="images/photo.jpg",
        verbose_name="Photo",
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Catéguorie"
    )
    creation_date = models.DateTimeField(auto_now_add=True)

    def has_promotion(self):
        # Vérifie s'il y a une promotion associée à ce produit
        return hasattr(self, "promotion") and self.promotion is not None

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"

    def __str__(self):
        return self.product_title

    def to_dict(self):
        return {
            "id": self.id,
            "product_title": self.product_title,
            "description": self.description,
            "price": str(self.price),
            "sale_price": str(self.sale_price) if self.sale_price else None,
            "price_before_discount": str(self.price_before_discount)
            if self.price_before_discount
            else None,
            "image": str(self.image),
            "creation_date": self.creation_date.isoformat(),
            "category": {
                "id": self.category.id,
                "category_title": self.category.category_title,
            },
        }


# Modèle Promotion
class Promotion(models.Model):
    start_date = models.DateField(verbose_name="Date de début")
    end_date = models.DateField(blank=True, verbose_name="Date de fin")
    discount_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Pourcentage de remise",
        validators=[MaxValueValidator(100)],
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name="Nom du produit"
    )

    class Meta:
        verbose_name = "Promotion"
        verbose_name_plural = "Promotions"

    def __str__(self):
        return f"{self.product.product_title} - {self.discount_percentage}% off"

    def is_active(self):
        today = date.today()
        return self.start_date <= today and (
            self.end_date is None or self.end_date >= today
        )

    def apply_discount(self):
        if self.is_active():
            # La promotion est active, donc nous appliquons la remise
            initial_price = self.product.price  # Le prix initial
            discount_percentage = self.discount_percentage
            new_price = initial_price - (initial_price * (discount_percentage / 100))

            # Mettre à jour le champ "price" (prix de vente) du produit
            self.product.price = new_price
            self.product.save()
