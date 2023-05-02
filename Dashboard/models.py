from django.db import models

# Create your models here.

class Notification(models.Model):
    message = models.CharField(max_length=120, null=False)
    date_occur = models.DateField(auto_now=True)
    status = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=70, null=True)

   