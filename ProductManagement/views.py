from django.shortcuts import render

# Create your views here.

def product_management(request):
  return render(request, 'UserInterface/product_management.html')