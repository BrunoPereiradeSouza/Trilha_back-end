# Generated by Django 5.0.6 on 2024-07-09 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_quantity_stocked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cover',
            field=models.ImageField(blank=True, default='', upload_to='products/covers/%Y/%m/%d/'),
        ),
    ]
