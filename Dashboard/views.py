from django.shortcuts import render, redirect
from  LoginAuthentication.models import CustomUser 

def dashboard(request):
  return render(request, 'UserInterface/dashboard.html', 
  context = {'User': CustomUser.objects.all(),
    
  })