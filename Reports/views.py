from django.shortcuts import render, redirect
from django.contrib import messages
from LoginAuthentication.models import CustomUser
from CustomerProfile.models import Customer
from ProductManagement.models import ProductCategory, TileSize, Product
from SalesTransaction.models import Transaction, Item, Installment
from django.db.models import Sum, Count
from ReturnProduct.models import ReturnItem
from AuditTrail.models import AuditTrail
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def reports(request):

  context = {
    'userForm': None,
    'cats': ProductCategory.objects.all(),
    'sizes': TileSize.objects.all(),
  }
  return render(request, 'UserInterface/reports.html', context)

@login_required(login_url='login')
def create_user_report(request):
  if request.method == 'GET':
    role = request.GET.get('urole')

    if role == "all" :
      
      request.session['um'] = 1

    elif role == "cashier":
      request.session['um'] = 2

    elif role == "admin":
      request.session['um'] = 3

    audit_log = AuditTrail(user=request.user, action=f'{request.user} has generated a users report.', location='Reports')
    audit_log.save()
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
  
  
  audit_log = AuditTrail(user=request.user, action=f'{request.user} has generated a customer report.', location='Reports')
  audit_log.save()

  return redirect('print_customer_report')
    


@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def create_sales_report(request):

  if request.method == 'GET':

    ttype = request.GET.get('ttype')
    inst = request.GET.get('inst')
    from_d = request.GET.get('from_d')
    to_d = request.GET.get('to_d')

    if ttype == 'all':

      if inst == 'true':
        request.session['sales'] = 1
        request.session['inst'] = "true"
        request.session['from'] = from_d
        request.session['to'] = to_d
      else:
        request.session['sales'] = 2
        request.session['inst'] = "false"
        request.session['from'] = from_d
        request.session['to'] = to_d
    else:
      if inst == 'true':
        request.session['sales'] = 3
        request.session['ttype'] = ttype
        request.session['from'] = from_d
        request.session['to'] = to_d
      else:
        request.session['sales'] = 4
        request.session['ttype'] = ttype
        request.session['from'] = from_d
        request.session['to'] = to_d
    audit_log = AuditTrail(user=request.user, action=f'{request.user} has generated a sales report.', location='Reports')
    audit_log.save()
    return redirect('all_transactions')

def sales_transaction_all(request):
      from_d = request.session['from']
      to_d = request.session['to']

      transactions = Transaction.objects.all()

      if request.session['sales'] == 1:
          transactions = Transaction.objects.filter(installment='true').filter(date_of_purchace__gte=from_d, date_of_purchace__lte=to_d).order_by('-total_price')
      elif request.session['sales'] == 2:
          transactions = Transaction.objects.filter(installment='false').filter(date_of_purchace__gte=from_d, date_of_purchace__lte=to_d).order_by('-total_price')
      elif request.session['sales'] == 3:
          ttype = request.session['ttype']

          transactions = Transaction.objects.filter(transaction_type=ttype).filter(installment='true').filter(date_of_purchace__gte=from_d, date_of_purchace__lte=to_d).order_by('-total_price')
      elif request.session['sales'] == 4:
          ttype = request.session['ttype']

          transactions = Transaction.objects.filter(transaction_type=ttype).filter(installment='false').filter(date_of_purchace__gte=from_d, date_of_purchace__lte=to_d).order_by('-total_price')


      context = {
        'transactions': transactions
      }
      return render(request, 'UserInterface/reports/print_sales.html', context)


def create_installments_report(request):
  ttype = request.GET.get('ttype')
  from_d = request.GET.get('from_d')
  to_d = request.GET.get('to_d')


  if ttype == 'all':
      request.session['installments'] = 1
      request.session['from_d'] = from_d
      request.session['to_d'] = to_d

  else:

      request.session['installments'] = 2
      request.session['from_d'] = from_d
      request.session['to_d'] = to_d
      request.session['ttype'] = ttype
  audit_log = AuditTrail(user=request.user, action=f'{request.user} has generated an installment report.', location='Reports')
  audit_log.save()
  return redirect('installment_report')

@login_required(login_url='login')
def print_installments(request):
      installments = Installment.objects.all().order_by('-date_paid')
      from_d = request.session['from_d']
      to_d = request.session['to_d']
      ttype = request.session['ttype']


      if request.session['installments'] == 1:
            installments = Installment.objects.filter(date_paid__gte=from_d, date_paid__lte=to_d).order_by('-date_paid')

      elif request.session['installments'] == 2:
            installments = Installment.objects.filter(payment_method=ttype).filter(date_paid__gte=from_d, date_paid__lte=to_d).order_by('-date_paid')

      context = {
        'installments' : installments,
      }

      return render(request, 'UserInterface/reports/print_installment_entries.html', context)


@login_required(login_url='login')
def create_product_report(request):

  if request.method == 'GET':
    cat = request.GET.get('cat')
    size = request.GET.get('size')
    from_d = request.GET.get('from_d')
    to_d = request.GET.get('to_d')

    if cat == 'all'  and size == 'all':
      request.session['prod'] = 1 

    elif cat != 'all' and size == 'all':
      request.session['prod'] = 2
      request.session['cat'] = cat  

    elif cat == 'all' and size != 'all':
      request.session['prod'] = 3
      request.session['size'] = size 

    elif cat != 'all' and size != 'all':
      request.session['prod'] = 4
      request.session['cat'] = cat 
      request.session['size'] = size 
    
    audit_log = AuditTrail(user=request.user, action=f'{request.user} has generated a product report.', location='Reports')
    audit_log.save()

    return redirect('product_report')



def create_top_selling_report(request):
  if request.method == 'GET':
    
    audit_log = AuditTrail(user=request.user, action=f'{request.user} has generated a top selling report.', location='Reports')
    audit_log.save()

    return redirect('top_selling_report')
  

@login_required(login_url='login')
def print_product_report(request):
   products = Product.objects.all().order_by('-id')
   cat = ""
   size = ""

   if request.session['prod'] == 1:
        products = Product.objects.all().order_by('category')
   elif request.session['prod'] == 2:
        cat = request.session['cat']
        products = Product.objects.filter(category=cat).order_by('product_size')
   elif request.session['prod'] == 3:
        size = request.session['size']
        products = Product.objects.filter(product_size=size).order_by('category')
   elif request.session['prod'] == 4:
        cat = request.session['cat']
        size = request.session['size']
        products = Product.objects.filter(category=cat).filter(product_size=size).order_by('category')

        if not products.exists():
          messages.error(request, 'Products not found')
          return redirect('reports')


   context = {
    'products': products,
   }

   return render(request, 'UserInterface/reports/print_product_report.html', context)

def print_top_selling_report(request):

   products = Item.objects.values('name', 'size').annotate(count=Count('transaction_no'), sold=Sum('pieces'), price=Sum('total')).order_by('-count')
   print(products)

   if not products.exists():
      messages.error(request, 'There are no top selling products at te moment')
      return redirect('reports')

   context = {
    'products': products,
   }
   return render(request, 'UserInterface/reports/top_selling.html', context)



def create_return_report(request):
    if request.method == 'GET':
      request.session['from_d'] = from_d = request.GET.get('from_d')
      request.session['to_d'] = to_d = request.GET.get('to_d')

      audit_log = AuditTrail(user=request.user, action=f'{request.user} has generated a returned product report.', location='Reports')
      audit_log.save()

      return redirect('return_product_report')



@login_required(login_url='login')
def return_product_report(request):
  from_d = request.session['from_d']
  to_d = request.session['to_d']

  returns = ReturnItem.objects.filter(date_returned__gte=from_d, date_returned__lte=to_d)

  context = {
    'returns': returns
  }

  return render(request, 'UserInterface/reports/return_item_report.html', context)


def create_audit_report(request):
    if request.method == 'GET':
        location = request.GET.get('location')
        from_d = request.GET.get('from_d')
        to_d = request.GET.get('to_d')


        if location == "all":
            request.session['audit'] = 1
            request.session['from_d'] = from_d
            request.session['to_d'] = to_d


        else:
            request.session['audit'] = 2
            request.session['location'] = location
            request.session['from_d'] = from_d
            request.session['to_d'] = to_d

        return redirect('audit_report')

@login_required(login_url='login')
def audit_report(request):
    audits = AuditTrail.objects.all().order_by('-timestamp')

    if request.session['audit'] == 2:
            from_date = request.session['from_d']
            to_d = request.session['to_d']
            location = request.session['location']
            audits = AuditTrail.objects.filter(location=location).order_by('-timestamp')
    
    context = {
      'audits': audits,
    }
    return render(request, 'UserInterface/reports/audit_reports.html', context)

