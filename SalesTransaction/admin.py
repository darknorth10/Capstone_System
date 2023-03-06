from django.contrib import admin
from .models import Transaction, Item
# Register your models here.

admin.site.register([Transaction, Item])