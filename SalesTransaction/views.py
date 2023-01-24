from django.shortcuts import render

# Create your views here.
def sales_transaction(request):
  return render(request, 'UserInterface/sales_transaction.html')