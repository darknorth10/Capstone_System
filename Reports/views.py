from django.shortcuts import render, redirect
from django.contrib import messages
from LoginAuthentication.models import CustomUser
from CustomerProfile.models import Customer
from ProductManagement.models import ProductCategory, TileSize
# Create your views here.
def reports(request):

  context = {
    'userForm': None,
    'cats': ProductCategory.objects.all(),
    'sizes': TileSize.objects.all(),
  }
  return render(request, 'UserInterface/reports.html', context)


def create_user_report(request):
  if request.method == 'GET':
    role = request.GET.get('urole')

    if role == "all" :
      
      request.session['um'] = 1

    elif role == "cashier":
      request.session['um'] = 2

    elif role == "admin":
      request.session['um'] = 3

    return redirect('print_user_report')


def create_customer_report(request):

  if request.method == 'GET':
    eligible = request.GET.get('eligible')

    if eligible == "all":
        request.session['eligible'] = 1
    elif eligible == "t" :
        request.session['eligible'] = 2
    else :
        request.session['eligible'] = 3
  

  return redirect('print_customer_report')
    



def print_user_report(request):
  user_print = CustomUser.objects.all().order_by('role')

  if request.session['um'] == 1 :
      user_print = CustomUser.objects.all().order_by('role')
  elif request.session['um'] == 2:
      user_print = CustomUser.objects.filter(role="cashier").order_by('first_name')
  elif request.session['um'] == 3 :
      user_print = CustomUser.objects.filter(role="admin").order_by('first_name')
  else :
        user_print = CustomUser.objects.all().order_by('role')

  context = {
    'User' : user_print
  }
  
  return render(request, 'UserInterface/reports/print_user_report.html', context)


def print_customer_report(request):

  customer_print = Customer.objects.all().order_by('first_name')

  if request.session['eligible'] == 1:
      customer_print = Customer.objects.all().order_by('first_name')
  elif request.session['eligible'] == 2:
      customer_print = Customer.objects.filter(eligibility=True)
  else:
      customer_print = Customer.objects.filter(eligibility=False)
 
  context = {
    'customers' : customer_print
  }
  


  return render(request, 'UserInterface/reports/print_customer.html', context)