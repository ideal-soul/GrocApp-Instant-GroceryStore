# Generated by Django 5.0.1 on 2024-01-10 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GrocApp', '0003_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]