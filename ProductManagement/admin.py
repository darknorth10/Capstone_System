from django.contrib import admin
from .models import Product, ProductArchive
# Register your models here.
admin.site.register([Product, ProductArchive])


