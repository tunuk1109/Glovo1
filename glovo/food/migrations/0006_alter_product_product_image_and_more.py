# Generated by Django 5.1.4 on 2025-01-19 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_alter_courier_current_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images'),
        ),
        migrations.AlterField(
            model_name='productcombo',
            name='combo_image',
            field=models.ImageField(blank=True, null=True, upload_to='combo_images'),
        ),
    ]
