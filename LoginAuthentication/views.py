from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import forms

# Create your views here.


def login_page(request):
  form = forms.LoginForm()
  message = ''
  
  if request.method == "POST":
    form = forms.LoginForm(request.POST)
    
    if form.is_valid():
      user = authenticate(
        username = form.cleaned_data['username'],
        password = form.cleaned_data['password'],
        )
      
      if user is not None:
        login(request, user)
        return redirect('dashboard')
      else:
        print("Wrong username or pass")
        message = "Wrong username or password"
        form = forms.LoginForm()
    else:
      form = forms.LoginForm()      
          
  return render(request, 'Login/login.html', context={'form': form, 'message': message})

#Logout view
def logout_user(request):
  logout(request)
  message = "You've been logged out."
  return render(request, 'Login/logout.html', context={'message':message})