from django.db import models

# Create your models here.

class ReturnItem(models.Model):
    name = models.CharField(max_length=80, null=False)
    size = models.CharField(max_length=40, null=False)
    quantity = models.IntegerField(null=False)
    transact_no = models.IntegerField(null=False)
    orig_quantity = models.IntegerField(null=True)
    description = models.TextField(null=True, max_length=80)
    date_returned = models.DateField(auto_now=True)