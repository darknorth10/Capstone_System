from django.shortcuts import render, redirect, get_object_or_404
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


def edit_customer(request, id):
    customer = Customer.objects.get(id=id)
    obj = get_object_or_404(Customer, id=id)

    editform = CustomerForm(request.POST or None, instance=obj)

    if request.method == 'POST':
        if editform.is_valid():

            editform.save()
            messages.success(request, 'Customer updated successfully')
            audit_log = AuditTrail(user=request.user, action=f'{request.user} has updated a customer.', location='Customer Profile')
            audit_log.save()
            return redirect('customer_profile')

    context = {
        'customer' : customer,
        'customer_form' : editform,
    }
    return render(request, 'UserInterface/edit_customer.html', context)