from django.shortcuts import render
from .models import Product
from .forms import ProductForm

# Create your views here.

def product_management(request):
  products = Product.objects.all()
  product_form = ProductForm()
  # product_form.fields['date_last_stocked'].widget.attrs.update({'required': 'false'})

  if request.method == 'POST':
    product_form = ProductForm(request.POST)
    if product_form.is_valid():
      product_form.save()
    else:
      product_form = ProductForm()
  return render(request, 'UserInterface/product_management.html', context={'products': products, 'product_form': product_form,})