from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ProductManagement.forms import SizeForm, CategoryForm
from ProductManagement.models import Product, TileSize, ProductCategory
from VisitorsPage.forms import PhoneForm, EmailForm, LocationForm
from VisitorsPage.models import Contact

# Create your views here.
def settings(request):

  obj = get_object_or_404(Contact, id=1)
  
  sizeform = SizeForm()
  catform = CategoryForm(auto_id='cat_%s')
  pform = PhoneForm(instance=obj)
  eform = EmailForm(instance=obj)
  lform = LocationForm(instance=obj)

  context = {
    'sizeform' : sizeform,
    'catform' : catform,
    'pform' : pform,
    'eform' : eform,
    'lform' : lform,
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


def update_phone(request):
  obj = get_object_or_404(Contact, id=1)

  if request.method == 'POST':
    form = PhoneForm(request.POST or None, instance=obj)

    if form.is_valid():
      form.save()
      messages.success(request, 'Contact updated successfully.')
      return redirect('settings')
    else:
      messages.error(request, 'Phone is not valid.')
      return redirect('settings')
def update_email  (request):
  obj = get_object_or_404(Contact, id=1)

  if request.method == 'POST':
    form = EmailForm(request.POST or None, instance=obj)

    if form.is_valid():
      form.save()
      messages.success(request, 'Email updated successfully.')
      return redirect('settings')
    else:
      messages.error(request, 'Email is not valid.')

      return redirect('settings')

def update_location(request):
  obj = get_object_or_404(Contact, id=1)

  if request.method == 'POST':
    form = LocationForm(request.POST or None, instance=obj)

    if form.is_valid():
      form.save()
      messages.success(request, 'Location updated successfully.')
      return redirect('settings')
    else:
      messages.error(request, 'Location is not valid.')
      return redirect('settings')