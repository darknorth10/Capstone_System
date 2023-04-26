from django.shortcuts import render
from .models import Customer
from .forms import CustomerForm
from django.contrib import messages
from AuditTrail.models import AuditTrail
# Create your views here.

def index(request):
    customers = Customer.objects.all()
    customers_form = CustomerForm()

    if request.method == 'POST':
        customers_form = CustomerForm(request.POST)
        if customers_form.is_valid():
            customers_form.save()
            customers_form = CustomerForm()
            messages.success(request, 'Customer profile has been registered')
            audit_log = AuditTrail(user=request.user, action=f'{request.user} has registered a regular customer.', location='Customer Profile')
            audit_log.save()
        else:
            print(customers_form.errors)

            def get_errors():
                for field, errors in customers_form.errors.items():
                    for error in errors:
                        return error
            messages.error(request, get_errors())
            
    return render(request, 'UserInterface/customerprofile.html', context = {'custom': Customer, 'customers': customers, 'customer_form': customers_form})