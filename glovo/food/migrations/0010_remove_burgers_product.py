# Generated by Django 5.1.5 on 2025-01-21 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0009_burgers_burger_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='burgers',
            name='product',
        ),
    ]
