from django.shortcuts import render, redirect
from ProductManagement.models import Product
from .models import Cart
from SalesTransaction.models import Transaction, Item, Installment
from .forms import CartQuantityForm, CashForm, GcashForm, BankingForm, BalanceForm
from django.db.models import Sum, Q
from django.contrib import messages
from django.http import JsonResponse
import locale
from AuditTrail.models import AuditTrail
from Dashboard.models import Notification
from django.core.mail import send_mail
from Dashboard.views import get_notifications
from django.contrib.auth.decorators import login_required

            
# search item by name on key up
def searchItems(request):
  
  if request.method == 'POST':
    itemName = request.POST.get('itemNameSearch')
    request.session['prod_name_search'] = itemName
    return JsonResponse({'success': itemName}, status=200)


@login_required(login_url='login')
def pointofsale(request):
  products = Product.objects.all().order_by('category')


  # sorts items by name or category when ajax request
  if 'prod_name_search' in request.session:
    itemName = request.session['prod_name_search']

    if itemName is not None :
      products = Product.objects.filter(Q(product_name__icontains=itemName) | Q(category__icontains=itemName))
    else :
      products = Product.objects.all().order_by('category')
    request.session['prod_name_search'] = None
  else:
    products = Product.objects.all().order_by('category')


  cart = Cart.objects.all()
  form = CartQuantityForm()

  if request.method == 'POST':
    form = CartQuantityForm(request.POST)
    
    if form.is_valid():
      prodID = form.cleaned_data['product_id']

      form.save()
      prod = Product.objects.get(id=prodID)

      price = prod.price
      quantity = form.cleaned_data['quantity']
      total_price = price * quantity
      cartitem = Cart.objects.filter(product_id=prodID)

      #  condition for multiple same product in a cart to avoid duplication in invoice list
      if cartitem.count() > 1:
        print("2 records")
        min = cartitem[0].id

        #check for smallest id to represent an item
        for carts in cartitem:
          if carts.id < min:
            min = carts.id
        
        base_cartitem = Cart.objects.get(id=min)
        if base_cartitem.quantity + quantity <= Product.objects.get(id=base_cartitem.product_id).current_stock:
          base_cartitem.quantity += quantity
          base_cartitem.total_price += total_price
          base_cartitem.save()
        else :
          messages.error(request, 'Desired quantity will exceed current stock')
        
        for carts in cartitem:
          if not carts.id == min:
            carts.delete()
          
      # normal saving of cart
      else:

        cartitem = Cart.objects.get(product_id=prodID)
        total_price = quantity * price
        item_name = prod.product_name
        item_size = prod.product_size

        cartitem.total_price = total_price
        cartitem.name = item_name
        cartitem.size = item_size

        cartitem.save()

      form = CartQuantityForm()

    else:
      print(form.errors)
      messages.error(request, "Desired quantity exceeds current stock of the product")

  # Subtotal Format from cart database  
  subtotal = Cart.objects.aggregate(subtotal_cart=Sum('total_price'))


  #render Subtotal
  if subtotal['subtotal_cart'] is not None:
    formatted_subtotal = "{:,}".format(subtotal['subtotal_cart'])
  else:
    formatted_subtotal = 0
  
  cashform = CashForm()
  gcashform = GcashForm(auto_id='gcash_%s')
  bankform = BankingForm(auto_id='bank_%s')
  get_notifications()

  context = {'products': products, 'carts': cart, 'form': form, 'subtotal': formatted_subtotal, 'subtotal_raw': subtotal['subtotal_cart'], 'cashform': cashform, 'gcashform': gcashform, 'bankform': bankform}

  return render(request, 'UserInterface/pos.html', context)


# delete item in cart ajax
def delete_item(request, id):

    cartItem = Cart.objects.get(id=id)

    print(cartItem)
    if Cart.objects.all().count() == 1:
      Cart.objects.all().delete()
      audit_log = AuditTrail(user=request.user, action=f'{request.user} has remove an item.', location='Point of Sale')
      audit_log.save()
      messages.success(request, 'Transaction has been cleared')
    else:
      cartItem.delete()

    return redirect('pos')



# clear current transaction
def pos_clear(request):

   if request.method == 'POST':
    Cart.objects.all().delete()
    audit_log = AuditTrail(user=request.user, action=f'{request.user} has cleared a transaction.', location='Point of Sale')
    audit_log.save()
    messages.success(request, 'Transaction has been cleared')
    return redirect('pos')


# New Cash MOP Transaction in the pos
def add_transaction(request):

  if request.method == 'POST':
    cashform = CashForm(request.POST)
    
    if cashform.is_valid():
       
       cashform.save()
       
      #grab lastest record in transaction database
       obj = Transaction.objects.filter(transaction_type='Cash').order_by('-transaction_no')[0]
       obj.total_products = Cart.objects.all().count()

       if obj.installment == "true":
          obj.status = "Pending"
          obj.installment_paid = obj.amount
       else:
          obj.amount
          obj.status = "Complete"
       obj.save()
       
       cart = Cart.objects.all()

        #transafer cart item to item transaction table
       for item in cart:
        cartTransactionNo = obj.transaction_no
        cartItemId = item.product_id
        cartItemName = item.name
        cartItemSize = item.size
        cartItemPieces = item.quantity
        cartItemTotal = item.total_price

        # update product stock
        product = Product.objects.get(id = cartItemId)
        product.current_stock -= cartItemPieces

        #make it unavailable if current stocks hits 0
        if product.current_stock <= 0:
          product.current_stock = 0
          product.availability = False

        product.save()

        # create transaction record
        itemX = Item(transaction_no=cartTransactionNo, product_id=cartItemId, name=cartItemName, size=cartItemSize, pieces=cartItemPieces, total=cartItemTotal)
        itemX.save()

      #del existing items in cart after saving
       Cart.objects.all().delete()
       messages.success(request, 'Transaction completed successfully')
       audit_log = AuditTrail(user=request.user, action=f'{request.user} has added a new cash transaction.', location='Point of Sale')
       audit_log.save()
       get_notifications()
       print('successfully added transaction')

    else:
      print(cashform.errors)
      messages.error(request, 'Error processing transaction')

  return redirect('pos')


# New Gcash transaction MOP
def add_gcash_transaction(request):

  if request.method == 'POST':
    gcashform = GcashForm(request.POST)
    
    if gcashform.is_valid():
       
       gcashform.save()
       
      #grab lastest record in transaction database
       obj = Transaction.objects.filter(transaction_type='Gcash').order_by('-transaction_no')[0]
       obj.total_products = Cart.objects.all().count()

       if obj.installment == "true":
          obj.status = "Pending"
          obj.installment_paid = obj.amount
       else:
          obj.status = "Complete"
       obj.save()
       
       cart = Cart.objects.all()

       for item in cart:
        cartTransactionNo = obj.transaction_no
        cartItemId = item.product_id
        cartItemName = item.name
        cartItemSize = item.size
        cartItemPieces = item.quantity
        cartItemTotal = item.total_price

        # update product stock
        product = Product.objects.get(id = cartItemId)
        product.current_stock -= cartItemPieces

        #make it unavailable if current stocks hits 0
        if product.current_stock <= 0:
          product.current_stock = 0
          product.availability = False

        product.save()

        # create transaction record
        itemX = Item(transaction_no=cartTransactionNo, product_id=cartItemId, name=cartItemName, size=cartItemSize, pieces=cartItemPieces, total=cartItemTotal)
        itemX.save()

      #del existing items in cart after saving
       obj.total_products = Cart.objects.all().count()
       obj.status = "Complete"
       obj.save()

       Cart.objects.all().delete()
       messages.success(request, 'Transaction completed successfully')
       audit_log = AuditTrail(user=request.user, action=f'{request.user} has added a new gcash transaction.', location='Point of Sale')
       audit_log.save()
       print('successfully added transaction')
       get_notifications()

    else:
      print(gashform.errors)
      messages.error(request, 'Error processing transaction')

  return redirect('pos')




def add_bank_transaction(request):

  if request.method == 'POST':
    bankform = BankingForm(request.POST)
    
    if bankform.is_valid():
       
       bankform.save()
       
      #grab lastest record in transaction database
       obj = Transaction.objects.filter(transaction_type='Banking').order_by('-transaction_no')[0]
       obj.total_products = Cart.objects.all().count()
       
       if obj.installment == "true":
          obj.status = "Pending"
          obj.installment_paid = obj.amount
       else:
          obj.status = "Complete"
       obj.save()


       cart = Cart.objects.all()

       for item in cart:
        cartTransactionNo = obj.transaction_no
        cartItemId = item.product_id
        cartItemName = item.name
        cartItemSize = item.size
        cartItemPieces = item.quantity
        cartItemTotal = item.total_price

        # update product stock
        product = Product.objects.get(id = cartItemId)
        product.current_stock -= cartItemPieces

        #make it unavailable if current stocks hits 0
        if product.current_stock <= 0:
          product.current_stock = 0
          product.availability = False

        product.save()

        # create transaction record
        itemX = Item(transaction_no=cartTransactionNo, product_id=cartItemId, name=cartItemName, size=cartItemSize, pieces=cartItemPieces, total=cartItemTotal)
        itemX.save()

        #del existing items in cart after saving
       Cart.objects.all().delete()
       messages.success(request, 'Transaction completed successfully')
       audit_log = AuditTrail(user=request.user, action=f'{request.user} has added a new bank transaction.', location='Point of Sale')
       audit_log.save()
       print('successfully added transaction')
       get_notifications()

    else:
      print(bankform.errors)
      messages.error(request, 'Error processing transaction')

  return redirect('pos')




def installment_view(request):
  balanceform = BalanceForm(auto_id='balance_%s')

  if request.method == 'POST':
    balanceform = BalanceForm(request.POST)

    if balanceform.is_valid():
      update_installment_paid = {};
      amount_paid = balanceform.cleaned_data['amount_paid']
      get_trans_id = balanceform.cleaned_data['transaction_reference']
      
      update_installment_paid = Transaction.objects.get(transaction_no = int(get_trans_id))
      
      if amount_paid > update_installment_paid.total_price - update_installment_paid.installment_paid or amount_paid <= 0 :
        print("Exceeded the balance amount")
        messages.error(request, 'Error Creating Transaction, Exceeded the balance amount')
        balanceform = BalanceForm(auto_id='balance_%s')
      else:
        if update_installment_paid.installment_paid + amount_paid <= update_installment_paid.total_price : # check the installment paid amount if less than total price
          update_installment_paid.installment_paid += amount_paid # update the installer paid amount
          
          #  if the the balance has been settled make its status as complete
          if update_installment_paid.installment_paid == update_installment_paid.total_price :
            update_installment_paid.status = "Complete"
          
          update_installment_paid.save() # save the transaction
          balanceform.save() # save the form
        else:
          messages.error(request, 'Error Creating Transaction, you excceeded the balance remaining')
          balanceform = BalanceForm(auto_id='balance_%s')
          return redirect('installment_view')

        
        balanceform = BalanceForm(auto_id='balance_%s')
        audit_log = AuditTrail(user=request.user, action=f'{request.user} has added a new payment for installment.', location='Point of Sale')
        audit_log.save()
        messages.success(request, 'Transaction completed successfully')
      
    else: # if not valid
        print(balanceform.errors)
        balanceform = BalanceForm(auto_id='balance_%s')
        messages.error(request, 'Error Creating Transaction, Transaction reference and payment method are required')
      


  context = {
    'installments': Transaction.objects.filter(status="Pending").filter(installment="true"),
    'entries' : Installment.objects.all().order_by('-transaction_no'),
    'balanceform' : balanceform,
  }

  return render(request, 'UserInterface/transactions/installments.html', context)



# sort items into porcelain in item drawer
def porcelain(request):
  porcelain = Product.objects.filter(category='Porcelain Tiles')
  return render(request, 'UserInterface/pos/porcelain.html')




