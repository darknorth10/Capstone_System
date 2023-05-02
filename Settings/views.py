from django.shortcuts import render, redirect
from django.contrib import messages
from ProductManagement.forms import SizeForm, CategoryForm
from ProductManagement.models import Product, TileSize, ProductCategory

# Create your views here.
def settings(request):

  sizeform = SizeForm()
  catform = CategoryForm(auto_id='cat_%s')

  context = {
    'sizeform' : sizeform,
    'catform' : catform,
  }

  return render(request, 'UserInterface/settings.html', context)



def addSize(request):

  if request.method == 'POST':

    sizeform = SizeForm(request.POST)

    if sizeform.is_valid():
      sizeform.save()
      messages.success(request, 'A new size was registered successfully.')

      return redirect('settings')

    else:
      messages.error(request, 'Error adding new size, size is already registered.')

      return redirect('settings')

def addCategory(request):

  if request.method == 'POST':

    catform = CategoryForm(request.POST)

    if catform.is_valid():
      catform.save()
      messages.success(request, 'A new product category was registered successfully.')

      return redirect('settings')

    else:
      messages.error(request, 'Error adding product category, category is already registered.')
      print(catform.errors)
      return redirect('settings')

