# Generated by Django 4.1.3 on 2023-05-01 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProductManagement', '0017_rename_size_productcategory_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TileSizes',
            new_name='TileSize',
        ),
    ]