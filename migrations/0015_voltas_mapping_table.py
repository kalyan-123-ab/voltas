# Generated by Django 5.0.6 on 2024-05-24 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voltasapp', '0014_mymodel_delete_imageupload'),
    ]

    operations = [
        migrations.CreateModel(
            name='voltas_mapping_table',
            fields=[
                ('sk', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('inv_vfx', models.TextField(blank=True, null=True)),
                ('tonnage', models.TextField(blank=True, null=True)),
                ('star_rating', models.TextField(blank=True, null=True)),
                ('series', models.TextField(blank=True, null=True)),
                ('fascia', models.TextField(blank=True, null=True)),
                ('material_code', models.TextField(blank=True, null=True)),
                ('model_name', models.TextField(blank=True, null=True)),
                ('mop', models.TextField(blank=True, null=True)),
                ('amazon_url', models.TextField(blank=True, null=True)),
                ('amazon_sku', models.TextField(blank=True, null=True)),
                ('flipkart_url', models.TextField(blank=True, null=True)),
                ('flipkart_sku', models.TextField(blank=True, null=True)),
                ('vijay_url', models.TextField(blank=True, null=True)),
                ('vijay_sku', models.TextField(blank=True, null=True)),
                ('croma_url', models.TextField(blank=True, null=True)),
                ('croma_sku', models.TextField(blank=True, null=True)),
                ('jiomart_url', models.TextField(blank=True, null=True)),
                ('jiomart_sku', models.TextField(blank=True, null=True)),
                ('reliance_url', models.TextField(blank=True, null=True)),
                ('reliance_sku', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'voltas_mapping_table',
            },
        ),
    ]
