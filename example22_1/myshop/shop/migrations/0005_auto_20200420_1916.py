# Generated by Django 3.0.4 on 2020-04-20 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20200420_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_sale',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
