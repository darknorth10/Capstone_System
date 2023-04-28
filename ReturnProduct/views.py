from django.shortcuts import render, redirect, get_object_or_404
from SalesTransaction.models import Transaction, Item
from ProductManagement.models import Product
from django.contrib import messages
from .forms import ReturnItemForm
from .models import ReturnItem
from AuditTrail.models import AuditTrail
# Create your views here.

# for the value of select element in return items list
def search_transaction(request):
  if request.method == 'POST':
    request.session['transact_no'] = request.POST.get('transac')
    return redirect('return_product')

def return_product(request):
  
  item_no = None
  tnum = 0
  
  if 'transact_no' in request.session:
    tnum = request.session['transact_no']
    err = ""
    if tnum is None or tnum == '':
      item_no = None
    else:
      checkTrans_number = Item.objects.filter(transaction_no=tnum).exists()
      if checkTrans_number :
            item_no = Item.objects.filter(transaction_no=tnum)
            messages.success(request, 'Transaction has been found.')
            audit_log = AuditTrail(user=request.user, action=f'{request.user} has search for a transaction to return an item.', location='Return Product')
            audit_log.save()
            print(item_no)
      else:
          item_no = None
          messages.error(request, "There is no match for the transaction number.")

    request.session['transact_no'] = None


  returnForm = ReturnItemForm(auto_id='return_%s')


  # return product if defected
  if request.method == 'POST':
    returnForm = ReturnItemForm(request.POST)
    
    if returnForm.is_valid():

      # deduct the exchanged product to current stock
      product = Product.objects.get(product_name=returnForm.cleaned_data['name'])
      print(product.current_stock)
      if returnForm.cleaned_data['quantity'] < product.current_stock:
        product.current_stock -= returnForm.cleaned_data['quantity']
        product.save()
         #save retturned item
        returnForm.save()
        messages.success(request, 'Item was successfully exchanged.')
        audit_log = AuditTrail(user=request.user, action=f'{request.user} has returned/exchanged an item.', location='Return Product')
        audit_log.save()
        returnForm = ReturnItemForm(auto_id='return_%s')

        # if the returned item is greater than the current stocks
      else:
        
        messages.error(request, "Error while returning item, quantity is greater than the current stocks")

    else:
      print(returnForm.errors )





  context = {
    'items' : item_no,
    'tnum' : tnum,
    'returnform': returnForm,
    'returnTable': ReturnItem.objects.all().order_by('-date_returned')
  }
  return render(request, 'UserInterface/return_product/return_product.html', context)
  