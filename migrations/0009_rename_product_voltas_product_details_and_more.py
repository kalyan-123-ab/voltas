# Generated by Django 5.0.6 on 2024-05-08 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voltasapp', '0008_alter_product_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Voltas_product_details',
        ),
        migrations.AlterModelTable(
            name='voltas_product_details',
            table='Voltas_product_details',
        ),
    ]
