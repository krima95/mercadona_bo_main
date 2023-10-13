from datetime import datetime

from django.db import models


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
    description = models.TextField(blank=True, verbose_name="Description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix")
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix soldé", null=True,
                                     blank=True)
    price_before_discount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix initial",
                                                null=True, blank=True)
    image = models.ImageField(blank=True, upload_to='images',
                              verbose_name="Photo")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Catéguorie")
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"

    def __str__(self):
        return self.product_title



class Promotion(models.Model):
    start_date = models.DateField(verbose_name="Date de début")
    end_date = models.DateField(blank=True, verbose_name="Date de fin")
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Pourcentage de remise")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Nom du produit")

    class Meta:
        verbose_name = "Promotion"
        verbose_name_plural = "Promotions"

    def __str__(self):
        return f"{self.product.product_title} - {self.discount_percentage}% off"

