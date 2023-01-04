from django.shortcuts import render

# Create your views here.
def return_product(request):
  return render(request, 'UserInterface/return_product.html')
  