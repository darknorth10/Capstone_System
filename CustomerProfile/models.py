from django.db import models
from django.core.validators import RegexValidator

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
    phone_number = models.CharField(max_length=11, validators=[RegexValidator(r'^\d{1,11}$')], null=True, blank=True)
    permanent_address = models.CharField(max_length=60, null=False)
    delivery_address = models.CharField(max_length=60, null=False)
    ELIGIBLE_CHOICES = [
        ('eligible', 'Eligible'),
        ('ineligible', 'Ineligible'),
    ]
    credit_eligibility = models.CharField(max_length=20, null=False, choices=ELIGIBLE_CHOICES)

    def __str__(self):
        return self.email
    
