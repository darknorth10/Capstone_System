from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, changeProductForm, addStocksForm
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.

def product_management(request):
  products = Product.objects.all()
  product_form = ProductForm()
  product_form.fields['product_name'].widget.attrs.update({'class': 'form-control', 'maxlength': '40'})
  product_form.fields['brand'].widget.attrs.update({'class': 'form-control', 'maxlength': '40'})
  product_form.fields['product_size'].widget.attrs.update({'class': 'role-select rounded'})
  product_form.fields['category'].widget.attrs.update({'class': 'role-select rounded'})
  product_form.fields['price'].widget.attrs.update({'class': 'form-control'})
  product_form.fields['current_stock'].widget.attrs.update({'class': 'form-control'})
  product_form.fields['availability'].widget.attrs.update({'class': 'form-check-input'})
  product_form.fields['product_img'].widget.attrs.update({'class': 'form-control'})

  if request.method == 'POST':
    product_form = ProductForm(request.POST, request.FILES)
    if product_form.is_valid():
      product_form.save()
      messages.success(request, 'Product registered successfully')
    else:
      print(product_form.errors)
      messages.error(request, 'Error registering product')


  return render(request, 'UserInterface/product_management.html', context={'products': products, 'product_form': product_form,})


def add_product(request):
  return

def edit_product(request, id):
  selected_product = Product.objects.get(id=id)
  obj = get_object_or_404(Product, id=id)
  product_form = changeProductForm(request.POST or None, request.FILES or None, instance=obj)
  product_form.fields['price'].widget.attrs.update({'class': 'form-control'})
  product_form.fields['availability'].widget.attrs.update({'class': 'form-check-input'})
  product_form.fields['product_img'].widget.attrs.update({'class': 'form-control'})
  
  if request.method == 'POST':
    if product_form.is_valid():
      product_form.save()
      messages.success(request, 'Product updated successfully')
      return redirect('product_management')
    else:
      print(product_form.errors)
      if product_form.non_field_errors():
        messages.error(request, product_form.non_field_errors())
      elif product_form.has_error('price'):
        messages.error(request, product_form.errors)
      

  return render(request, 'UserInterface/editproduct.html', context  = {'product': selected_product, 'product_form': product_form,})

  # for adding stocks
def add_stock(request, id):
  selected_product = Product.objects.get(id=id)
  obj = get_object_or_404(Product, id=id)
  form = addStocksForm(request.POST)
  form.fields['current_stock'].widget.attrs.update({'class': 'form-control', 'required': 'required',  })

  if request.method == 'POST':
    if form.is_valid():
      new_stock = selected_product.current_stock + form.cleaned_data['current_stock']
      print(new_stock)

      selected_product.current_stock = new_stock
      selected_product.save()
      messages.success(request, 'Stocks are successfully added.')
      return redirect('product_management')
    else:
      print(form.errors)

  return render(request, 'UserInterface/addProductStock.html', context = {'product':selected_product, 'form': form,})