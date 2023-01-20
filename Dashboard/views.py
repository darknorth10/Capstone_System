from django.shortcuts import render, redirect
from  LoginAuthentication.models import CustomUser 
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def dashboard(request):
  return render(request, 'UserInterface/dashboard.html', 
  context = {'User': CustomUser.objects.all(),
    
  })