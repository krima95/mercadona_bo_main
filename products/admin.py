from django.contrib import admin
from products.models import Category, Product, Promotion


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'product_title', 'price')
    list_filter = ('category', 'product_title')
    search_fields = ['product_title', 'price']
    list_per_page = 10


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('product', 'discount_percentage', 'start_date', 'end_date')
    list_filter = ['product', 'discount_percentage', 'start_date', 'end_date']
    search_fields = ['discount_percentage', 'start_date', 'end_date']
    list_per_page = 10


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_title',)
    search_fields = ['category_title']
    list_per_page = 10



