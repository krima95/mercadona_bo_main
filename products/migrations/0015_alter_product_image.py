# Generated by Django 4.2.6 on 2023-10-16 10:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0014_alter_promotion_discount_percentage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True, upload_to="images/", verbose_name="Photo"
            ),
        ),
    ]