from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=20, null=False)
    brand = models.CharField(max_length=20, null=False)
    SIZES = [
        ('20x20', '20 x 20'),
        ('30x30', '30 x 30'),
    ]
    product_size = models.CharField(max_length=10, null=True, choices=SIZES)
    CATEGORIES  = [
        ('Porcelain Tiles', 'Porcelain Tiles'),
        ('Ceramic Tiles', 'Ceramic Tiles'),
        ('Adhesive', 'Adhesive'),
        ('Sanitary Wares', 'Sanitary Wares'),
    ]
    category = models.CharField(max_length=20, null=False, choices=CATEGORIES)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    current_stock = models.PositiveIntegerField(null=False)
    date_last_stocked = models.DateTimeField(null=True, auto_now_add=True)
    availability = models.BooleanField(default=True)
    def __str__(self):
        return self.product_name