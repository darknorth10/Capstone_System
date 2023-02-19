from django.shortcuts import render
from .models import Customer
from .forms import CustomerForm
# Create your views here.

def index(request):
    customers = Customer.objects.all()
    customers_form = CustomerForm()

    if request.method == 'POST':
        customers_form = CustomerForm(request.POST)
        if customers_form.is_valid():
            customers_form.save()
        else:
            print(customers_form.errors)
            customers_form = CustomerForm()
    return render(request, 'UserInterface/customerprofile.html', context = {'custom': Customer, 'customers': customers, 'customer_form': customers_form})