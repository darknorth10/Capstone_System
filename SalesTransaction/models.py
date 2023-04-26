from django.db import models
from ProductManagement.models import Product
from django.core.validators import RegexValidator
from datetime import datetime, timedelta
# Create your models here.

class Transaction(models.Model):
    transaction_no = models.BigAutoField(primary_key=True)
    TYPE_CHOICES = [
        ('Cash', 'Cash'),
        ('Gcash', 'Gcash'),
        ('Banking', 'Banking'),
    ]
    transaction_type = models.CharField(max_length=20, null=False, choices=TYPE_CHOICES)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, null=False)
    total_products = models.PositiveIntegerField(null=True, blank=True)
    date_of_purchace = models.DateTimeField(auto_now_add=True, null=False)
    delivery_address = models.CharField(max_length=80, null=True, blank=True)

    #payment
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    change = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, default=0.00)
    customer_name = models.CharField(max_length=30, null=True, blank=True)
    contact = models.CharField(max_length=11, null=True, blank=True)
    email = models.EmailField(max_length=40, null=True, blank=True)
    reference_no = models.CharField(max_length=40, null=True, blank=True)
    gcash_no = models.CharField(max_length=11, validators=[RegexValidator(r'^\d{1,11}$')], null=True, blank=True)

    BANKING_CHOICES = [
        ('Credit', 'Credit'),
        ('Debit', 'Debit'),
        ('Cheque', 'Cheque'),
    ]
    account_name = models.CharField(max_length=45, null=True, blank=True)
    banking_type = models.CharField(max_length=15, null=True, blank=True, choices=BANKING_CHOICES)
    bank_name = models.CharField(max_length=60, null=True, blank=True)
    STATUS_CHOICES = [
        ('Complete', 'Complete'),
        ('Pending', 'Pending'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, null=True, blank=True)
    ORDER_CHOICES = [
        ('Delivery', 'Delivery'),
        ('Pickup', 'Pickup'),
    ]
    order_type = models.CharField(max_length=10, choices=ORDER_CHOICES  , null=True, blank=True)

    installment = models.CharField(max_length=10, blank=True, null=True, default='false')
    installment_paid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0.00)
    installment_due = models.DateTimeField(default=datetime.now()+timedelta(days=30))
    
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


class Installment(models.Model):
    transaction_no = models.BigAutoField(primary_key=True)
    transaction_reference = models.IntegerField(null=True, blank=True) # hidden
    customer_name = models.CharField(max_length=45, null=True, blank=True)
    amount_paid = models.DecimalField(null=False, decimal_places=2, max_digits=10)
    date_paid = models.DateField(auto_now=True) #not included in form
    
    TYPE_CHOICES = [
        ('false', '----- Select Payment Method -----'),
        ('Cash', 'Cash'),
        ('Gcash', 'Gcash'),
        ('Banking', 'Banking'),
    ]

    payment_method = models.CharField(max_length=20, null=False, choices=TYPE_CHOICES, default="false")
    reference_no = models.CharField(max_length=40, null=True, blank=True)
