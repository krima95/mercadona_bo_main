# Generated by Django 4.2.6 on 2023-10-16 15:10

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0017_alter_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True,
                default="photo.jpg",
                null=True,
                storage=django.core.files.storage.FileSystemStorage(
                    location="/media/images"
                ),
                upload_to="",
                verbose_name="Photo",
            ),
        ),
    ]
