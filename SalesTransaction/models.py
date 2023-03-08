from django.db import models
from ProductManagement.models import Product
# Create your models here.

class Transaction(models.Model):
    transaction_no = models.BigAutoField(primary_key=True)
    TYPE_CHOICES = [
        ('Cash', 'Cash'),
        ('Gcash', 'Gcash'),
        ('Installment', 'Installment'),
        ('Banking', 'Banking'),
    ]
    transaction_type = models.CharField(max_length=20, null=False, choices=TYPE_CHOICES)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, null=False)
    total_products = models.PositiveIntegerField(null=True, blank=True)
    date_of_purchace = models.DateTimeField(auto_now_add=True, null=False)
    delivery_address = models.CharField(max_length=80, null=True)

    #payment
    amount = models.DecimalField(max_digits=9, decimal_places=2, null=False)
    change = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    customer_name = models.CharField(max_length=30, null=False)
    contact = models.CharField(max_length=11, null=False)
    email = models.EmailField(max_length=40, null=True, blank=True)
    reference_no = models.CharField(max_length=40, null=True, blank=True)

    STATUS_CHOICES = [
        ('complete', 'Complete'),
        ('pending', 'Pending'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return str(self.transaction_no)

class Item(models.Model):
    transaction_no = models.IntegerField(null=False)
    product_id = models.IntegerField(null=False)
    name = models.CharField(max_length=45, null=False)
    size = models.CharField(max_length=15, null=False)
    pieces = models.PositiveIntegerField(null=False)
    total = models.DecimalField(max_digits=9, decimal_places=2, null=False)

    def __str__(self):
        return "Item for Transaction no. " + str(self.transaction_no)

