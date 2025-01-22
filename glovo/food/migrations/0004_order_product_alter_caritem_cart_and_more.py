# Generated by Django 5.1.4 on 2025-01-19 10:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_remove_product_category_store_store_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='food.product'),
        ),
        migrations.AlterField(
            model_name='caritem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_cart_item', to='food.cart'),
        ),
        migrations.AlterField(
            model_name='productcombo',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='combo', to='food.store'),
        ),
        migrations.AlterField(
            model_name='store',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_store', to='food.category'),
        ),
    ]
