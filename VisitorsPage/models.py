from django.db import models

# Create your models here.

class Contact(models.Model):
     phone = models.CharField(max_length=15, null=True)
     email = models.EmailField(max_length=20, null=True)
     location = models.CharField(max_length=120, null=True)