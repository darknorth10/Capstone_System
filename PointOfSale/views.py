from django.shortcuts import render, redirect
from ProductManagement.models import Product
from .models import Cart
from .forms import CartQuantityForm
from django.db.models import Sum
from django.contrib import messages
import locale
# Create your views here.

def pointofsale(request):
  products = Product.objects.all()
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
        base_cartitem.quantity += quantity
        base_cartitem.total_price += total_price
        base_cartitem.save()
        
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
      print('error')
      print(form.errors)

  # Subtotal Format from cart database  
  subtotal = Cart.objects.aggregate(subtotal_cart=Sum('total_price'))
  
  if subtotal['subtotal_cart'] is not None:
    formatted_subtotal = "{:,}".format(subtotal['subtotal_cart'])
  else:
    formatted_subtotal = 0

  return render(request, 'UserInterface/pos.html', context = {'products': products, 'carts': cart, 'form': form, 'subtotal': formatted_subtotal,})


def porcelain(request):
  porcelain = Product.objects.filter(category='Porcelain Tiles')
  return render(request, 'UserInterface/pos/porcelain.html')


def pos_clear(request):
   if request.method == 'POST':
    Cart.objects.all().delete()
    messages.success(request, 'Transaction has been cleared')
    return redirect('pos')