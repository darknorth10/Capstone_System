from django.shortcuts import render
from .models import Customer
# Create your views here.

def index(request):
    customers = Customer.objects.all()

    return render(request, 'UserInterface/customerprofile.html', context = {'custom': Customer, 'customers': customers})