from django.shortcuts import render, redirect
from  LoginAuthentication.models import CustomUser 
from django.contrib.auth.decorators import login_required
from ProductManagement.models import Product
from SalesTransaction.models import Transaction

@login_required(login_url='login')
def dashboard(request):
  
  product_count = Product.objects.all().count()
  total_transactions = Transaction.objects.all().count()


  return render(request, 'UserInterface/dashboard.html', 
  context = {'User': CustomUser.objects.all(),
    'product_registered': product_count,
    'total_transactions': total_transactions,
  })