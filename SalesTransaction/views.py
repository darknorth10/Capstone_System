from django.shortcuts import render
from .models import Transaction, Item
# Create your views here.
 
def sales_transaction(request):
  transactions = Transaction.objects.all()
  payments = Transaction.objects.all()
  items = Item.objects.all()


  return render(request, 'UserInterface/transactions/sales_transaction.html', context = {'transactions': transactions, 'payments': payments, 'items': items})


def payment_info(request):
  payment = Transaction.objects.all()
  return render(request, 'UserInterface/transactions/payment_info.html', context = {'payment': payment,})

def items_transaction(request, id):
  item = Item.objects.get(id=id)
  return render(request, 'UserInterface/transactions/item_info.html', context = {'item': item,})