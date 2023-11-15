from rest_framework import serializers
from .models import Category, Product, Promotion


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "id",
            "product_title",
            "description",
            "price",
            "sale_price",
            "price_before_discount",
            "image",
            "category",
            "creation_date",
        )

    def get_category(self, obj):
        return {"id": obj.category.id, "category_title": obj.category.category_title}


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = "__all__"
