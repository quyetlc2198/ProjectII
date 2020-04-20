# Generated by Django 3.0.4 on 2020-04-20 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_price_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_sale',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10),
        ),
    ]