import pytest
from datetime import date, timedelta
from products.models import Category, Product, Promotion


# test ajouter une catégorie
@pytest.mark.django_db
def test_create_category():
    category = Category.objects.create(category_title="Test Category")
    assert str(category) == "Test Category"


# test créer un produit
@pytest.mark.django_db
def test_create_product():
    category = Category.objects.create(category_title="Test Category")
    product = Product.objects.create(
        product_title="Test Product",
        description="Test Description",
        price=10.0,
        category=category,
    )
    assert str(product) == "Test Product"


# test ajouter une promotion
@pytest.mark.django_db
def test_create_promotion():
    category = Category.objects.create(category_title="Test Category")
    product = Product.objects.create(
        product_title="Test Product",
        description="Test Description",
        price=10.0,
        category=category,
    )
    promotion = Promotion.objects.create(
        start_date=date.today(),
        discount_percentage=20.0,
        product=product,
    )
    assert str(promotion) == "Test Product - 20.0% off"


# test vérifier une promotion ajoutée
@pytest.mark.django_db
def test_has_promotion():
    category = Category.objects.create(category_title="Test Category")
    product = Product.objects.create(
        product_title="Test Product",
        description="Test Description",
        price=10.0,
        category=category,
    )
    promotion = Promotion.objects.create(
        start_date=date.today(),
        discount_percentage=20.0,
        product=product,
    )
    assert product.has_promotion() is True


@pytest.mark.django_db
def test_is_active_promotion():
    category = Category.objects.create(category_title="Test Category")
    product = Product.objects.create(
        product_title="Test Product",
        description="Test Description",
        price=10.0,
        category=category,
    )
    promotion = Promotion.objects.create(
        start_date=date.today(),
        end_date=date.today() + timedelta(days=10),
        discount_percentage=20.0,
        product=product,
    )
    assert promotion.is_active() is True


@pytest.mark.django_db
def test_apply_discount():
    category = Category.objects.create(category_title="Test Category")
    product = Product.objects.create(
        product_title="Test Product",
        description="Test Description",
        price=10.0,
        category=category,
    )
    promotion = Promotion.objects.create(
        start_date=date.today(),
        end_date=date.today() + timedelta(days=10),
        discount_percentage=20.0,
        product=product,
    )
    product_price_before_discount = product.price
    promotion.apply_discount()
    product.refresh_from_db()
    assert product.price != product_price_before_discount
    assert abs(product.price - product_price_before_discount * 0.8) < 0.01
