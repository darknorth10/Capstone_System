# Generated by Django 4.2 on 2023-04-16 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductManagement', '0012_productarchive_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Porcelain Tiles', 'Porcelain Tiles'), ('Ceramic Tiles', 'Ceramic Tiles'), ('Adhesive', 'Adhesive'), ('Tile Grout', 'Tile Grout'), ('Sanitary Wares', 'Sanitary Wares')], max_length=20),
        ),
    ]
