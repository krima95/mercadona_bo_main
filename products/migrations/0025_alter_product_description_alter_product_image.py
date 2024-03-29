# Generated by Django 4.2.6 on 2023-11-15 14:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0024_product_price_before_discount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(verbose_name="Description"),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True,
                default="images/photo.jpg",
                upload_to="images/",
                verbose_name="Photo",
            ),
        ),
    ]
