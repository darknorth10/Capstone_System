from django.shortcuts import render, redirect
from LoginAuthentication.models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def user_management(request):
  form_adduser = CustomUserCreationForm()
  if request.method == "POST":
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('usermanagement')
      
  return render(request, 'UserInterface/user_management.html',
    context = { 'Users': CustomUser.objects.all(), 'form': form_adduser }
  )