from django.db import models

# Create your models here.
class Customer(models.Model):
    last_name = models.CharField(max_length=20, null=False)
    first_name = models.CharField(max_length=40, null=False)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    sex = models.CharField(max_length=10, null=False, choices=GENDER_CHOICES)
    birthdate = models.DateField(auto_now=False, auto_now_add=False, null=False)
    email = models.EmailField(max_length=40)
    phone_number = models.CharField(max_length=11)
    permanent_address = models.CharField(max_length=60, null=False)
    delivery_address = models.CharField(max_length=60, null=False)
    credit_eligibility = models.BooleanField(default=True, null=False)

    def __str__(self):
        return self.email
    
