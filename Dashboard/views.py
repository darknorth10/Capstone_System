from django.shortcuts import render, redirect, get_object_or_404, Http404
from  LoginAuthentication.models import CustomUser 
from django.contrib.auth.decorators import login_required
from ProductManagement.models import Product
from SalesTransaction.models import Transaction, Item
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.db.models import Sum, Count
from django.utils import timezone
import datetime



@login_required(login_url='login')
def dashboard(request):
  current_year = timezone.now().year
  current_month = timezone.now().month

  product_count = Product.objects.all().count()
  total_transactions = Transaction.objects.all().count()

  # top 3 selling  items
  products = Item.objects.values('name').annotate(count=Count('transaction_no')).order_by('-count')[:3]

  # sales_month2 = Transaction.objects.filter(date_of_purchace__year=current_year).aggregate(Sum('total_price'))
  # sales_month = Transaction.objects.filter(date_of_purchace__month__gte=current_month, date_of_purchace__year__gte=current_year, date_of_purchace__month__lte=current_month, date_of_purchace__year__lte=current_year).aggregate(Sum('total_price'))
  sales_month = Transaction.objects.filter(date_of_purchace__year=current_year, date_of_purchace__month=current_month).aggregate(Sum('total_price'))
  sales_today = Transaction.objects.filter(date_of_purchace__day=timezone.now().day).aggregate(Sum('total_price'))
  today = 0
  curr_month = 0

  if sales_today.get('total_price__sum') is not None:
    today = sales_today.get('total_price__sum')
  if sales_month.get('total_price__sum') is not None:
    curr_month = sales_month.get('total_price__sum')

  formatted_sales_today = "{:,}".format(today)
  formatted_sales_month = "{:,}".format(curr_month)
  print(formatted_sales_month)
  print(formatted_sales_today)


  return render(request, 'UserInterface/dashboard.html', 
  context = {'User': CustomUser.objects.all(),
    'product_registered': product_count,
    'total_transactions': total_transactions,
    'top1' : products[0],
    'top2' : products[1],
    'top3' : products[2],
    'current_month_sales' : formatted_sales_month,
    'current_sales_today' : formatted_sales_today,
  })


@login_required(login_url='login')
def force_change_password(request, id):

  form = PasswordChangeForm(request.user)

  curr_user  = get_object_or_404(CustomUser, id=id)
  
  if request.method == 'POST':
    form = PasswordChangeForm(request.user, request.POST)

    if form.is_valid():

      curr_user.is_default = False
      curr_user.password = make_password(form.cleaned_data['new_password1'])

      curr_user.save()

      messages.success(request, "Password changed successfully.")
    else:
      print(form.errors)
      messages.error(request, "Correct the information below")

  context = {
    'form' : form,
    'curr_user' : curr_user,
  }
  return render(request, 'UserInterface/force_change_password.html', context)


def error_404_view(request, exception):
  return render(request, '404.html')