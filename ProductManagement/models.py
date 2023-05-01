from django.db import models


# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=40, null=False, unique=True)
    brand = models.CharField(max_length=40, null=False)

    product_size = models.CharField(max_length=10, null=True)
    
    category = models.CharField(max_length=20, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    current_stock = models.PositiveIntegerField(null=False)
    max_stock = models.PositiveIntegerField(null=True)
    date_last_stocked = models.DateField(null=True, auto_now_add=True)
    availability = models.BooleanField(default=True) 
    product_img = models.ImageField(upload_to='product_images', default='Dunmark.png')

class TileSize(models.Model):
    size = models.CharField(max_length=10, null=False, primary_key=True)
    
    def __str__(self):
        return self.size

class ProductCategory(models.Model):
    category = models.CharField(max_length=20, null=False, primary_key=True)

    def __str__(self):
        return self.category

class ProductArchive(models.Model):
    product_no = models.IntegerField(null=False)
    name = models.CharField(max_length=80, null=False)
    brand = models.CharField(max_length=80, null=True)
    category = models.CharField(max_length=80, null=False)
    size = models.CharField(max_length=80, null=False)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=False)
    stocks = models.IntegerField(null=False)
    date_archived = models.DateField(auto_now_add=True)
    product_img = models.ImageField(upload_to='product_archives', default='Dunmark.png')


    def __str__(self):
        return "Archive for Prod no. " + str(self.product_no)