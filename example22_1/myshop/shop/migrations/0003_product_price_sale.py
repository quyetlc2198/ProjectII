# Generated by Django 3.0.4 on 2020-04-16 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200403_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_sale',
            field=models.DecimalField(decimal_places=3, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]