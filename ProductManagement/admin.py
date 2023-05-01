from django.contrib import admin
from .models import Product, ProductArchive, TileSize, ProductCategory
# Register your models here.
admin.site.register([Product, ProductArchive, TileSize, ProductCategory])


