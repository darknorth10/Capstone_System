from django.shortcuts import render, redirect, get_object_or_404, Http404
from  LoginAuthentication.models import CustomUser 
from django.contrib.auth.decorators import login_required
from ProductManagement.models import Product
from SalesTransaction.models import Transaction, Item
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.db.models import Sum, Count, Q
from django.utils import timezone
import datetime



@login_required(login_url='login')
def dashboard(request):
  current_year = timezone.now().year
  current_month = timezone.now().month

  product_count = Product.objects.all().count()
  total_transactions = Transaction.objects.all().count()

  products = Product.objects.all()
  product_stock_level = Product.objects.all()[:5]

  if Item.objects.values('name').annotate(count=Count('transaction_no')).order_by('-count').count() >= 3:
      products = Item.objects.values('name').annotate(count=Count('transaction_no')).order_by('-count')[:5]

  if Item.objects.values('name').annotate(count=Count('name')).order_by('-count').count() >= 5:
      product_stock_level = Product.objects.filter(Q(product_name=products[0]['name']) | Q(product_name=products[1]['name']) | Q(product_name=products[2]['name']) | Q(product_name=products[3]['name']) | Q(product_name=products[4]['name']))

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
 


  return render(request, 'UserInterface/dashboard.html', 
  context = {'User': CustomUser.objects.all(),
    'product_registered': product_count,
    'total_transactions': total_transactions,
    'top1' : products[0],
    'top2' : products[1],
    'top3' : products[2],
    'prod1': product_stock_level[0],
    'prod2': product_stock_level[1],
    'prod3': product_stock_level[2],
    'prod4': product_stock_level[3],
    'prod5': product_stock_level[4],

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