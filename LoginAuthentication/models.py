from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = [
  ("cashier", "Cashier"),
  ("admin", "Admin"),
  ]

class CustomUser(AbstractUser):
  role = models.CharField(max_length=7, choices=ROLE_CHOICES, default="Cashier")
  
  def __str__(self):
    return self.username