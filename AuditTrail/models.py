from django.db import models

# Create your models here.

class AuditTrail(models.Model):
    user = models.CharField(max_length=45, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=90, null=False)
    location = models.CharField(max_length=60, null=False)