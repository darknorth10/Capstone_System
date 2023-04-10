from django.contrib import admin
from .models import Transaction, Item, Installment
# Register your models here.

admin.site.register([Transaction, Item, Installment])