from django.shortcuts import render

# Create your views here.

def pointofsale(request):
  return render(request, 'UserInterface/pos.html')