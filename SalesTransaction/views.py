from django.shortcuts import render
from django.http import JsonResponse
from .models import Transaction, Item
# Create your views here.
 
def sales_transaction(request):
  transactions = Transaction.objects.all().order_by('-transaction_no')
  payments = Transaction.objects.all()

  if request.method == 'POST':
    return JsonResponse({'success': True}, status=200)
  # transaction_no = 0
  context = {'transactions': transactions, 'payments': payments}


  return render(request, 'UserInterface/transactions/sales_transaction.html', context)

def view_detailed(request, id):
  item = Item.objects.filter(transaction_no=id)
  
  return render(request, 'UserInterface/transactions/detailed_transaction.html', context = {'items': item})

def payment_info(request):
  payment = Transaction.objects.all().order_by('-transaction_no')

  return render(request, 'UserInterface/transactions/payment_info.html', context = {'payment': payment,})

 