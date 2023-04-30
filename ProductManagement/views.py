from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductArchive
from .forms import ProductForm, changeProductForm, addStocksForm
from django.contrib import messages
from datetime import date
from django.http import JsonResponse
from django.db.models import Q
from AuditTrail.models import AuditTrail
# Create your views here.

def searchProduct(request):
  if request.method == 'POST':
    search_productName = request.POST.get('prodName')
    request.session['search_product'] = search_productName
    return JsonResponse({'success': True, 'test': search_productName}, status=200)

def product_management(request):
  products = Product.objects.all().order_by('category')

  # products with 0 stock will updated to unavailable
  

  # add product form attribute
  product_form = ProductForm()


  if request.method == 'POST':
    product_form = ProductForm(request.POST, request.FILES)
    if product_form.is_valid():
      product_form.save()
      messages.success(request, 'Product registered successfully')
      audit_log = AuditTrail(user=request.user, action=f'{request.user} has registered a new product.', location='Product Management')
      audit_log.save()
      product_form = ProductForm()
    else:
      print(product_form.errors)
      messages.error(request, 'Error registering product')

  for product in products:
    if product.current_stock <= 0:
      product.current_stock = 0
      product.availability = False
      product.save()
  
  # search for products

  if 'search_product' in request.session :
      search_term = request.session['search_product']

      if search_term is not None :
        products = Product.objects.filter(Q(product_name__icontains=search_term) | Q(category__icontains=search_term) ).order_by('category')
        print(request.session['search_product'])
      else :
        products = Product.objects.all().order_by('category')
      

  else :
    products = Product.objects.all().order_by('category')
    print("no session")

  request.session['search_product'] = None
  return render(request, 'UserInterface/product_management.html', context={'products': products, 'product_form': product_form,})


def edit_product(request, id):
  selected_product = Product.objects.get(id=id)
  obj = get_object_or_404(Product, id=id)
  product_form = changeProductForm(request.POST or None, request.FILES or None, instance=obj)
  product_form.fields['price'].widget.attrs.update({'class': 'form-control'})
  product_form.fields['availability'].widget.attrs.update({'class': 'form-check-input'})
  product_form.fields['product_img'].widget.attrs.update({'class': 'form-control'})
  product_form.fields['category'].widget.attrs.update({'class': 'role-select'})
  
  if request.method == 'POST':
    if product_form.is_valid():
      product_form.save()
      messages.success(request, 'Product updated successfully')
      audit_log = AuditTrail(user=request.user, action=f'{request.user} has updated a product.', location='Product Management')
      audit_log.save()
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
      # update current stocks
      selected_product.current_stock = new_stock
      selected_product.date_last_stocked = date.today()
      selected_product.save()
      print(date.today())
      # make the product aavailable when restocked and greater than 0
      if selected_product.current_stock >= 0:
        selected_product.availability = True
        selected_product.save()
        
      messages.success(request, 'Stocks are successfully added.')
      audit_log = AuditTrail(user=request.user, action=f'{request.user} has added a stock on a product.', location='Product Management')
      audit_log.save()
      return redirect('product_management')
    else:
      print(form.errors)
      messages.error(request, f"{form.non_field_errors().as_text()} {form.errors.as_text()}")

  return render(request, 'UserInterface/addProductStock.html', context = {'product':selected_product, 'form': form,})



def void_product(request):
  if request.method == 'POST':
    voidProdName = request.POST.get('voidName')
    obj = get_object_or_404(Product, product_name=voidProdName)
    voidProduct =ProductArchive(product_no = obj.id, name=obj.product_name, brand=obj.brand, category=obj.category, size=obj.product_size, price=obj.price, stocks=obj.current_stock, product_img=obj.product_img)
    voidProduct.save()
    obj.delete()
    messages.success(request, "An Item has been moved to the archives.")
    audit_log = AuditTrail(user=request.user, action=f'{request.user} has voided a product.', location='Product Management')
    audit_log.save()
    return redirect('product_management')


def archive_product(request):
  archives = ProductArchive.objects.all()
  context = {
    'archives': archives
  }
  return render(request, 'UserInterface/product_archives.html', context)