from django.shortcuts import render, redirect
from LoginAuthentication.models import CustomUser
from django.contrib.auth.decorators import login_required
from LoginAuthentication.forms import CustomUserCreationForm

# Create your views here.
@login_required(login_url='login')
def user_management(request):

  #instance of user creation form for creating user
  form_adduser = CustomUserCreationForm()

  #for addingg required attribute on to the inpu fields that are not required by default
  form_adduser.fields['first_name'].widget.attrs.update({'required': True})
  form_adduser.fields['last_name'].widget.attrs.update({'required': True})
  form_adduser.fields['email'].widget.attrs.update({'required': True})
  form_adduser.fields['password1'].widget.attrs.update({'pattern': '/(?=.*\d)(?=.*[a-z]).{8,}/i'})
  form_adduser.fields['password2'].widget.attrs.update({'pattern': '/(?=.*\d)(?=.*[a-z]).{8,}/i', 'minlength': '8'})

  if request.method == "POST":
    form_adduser = CustomUserCreationForm(request.POST)
    if form_adduser.is_valid():
      form_adduser.save()

    else:
      print("error")
      
  return render(request, 'UserInterface/user_management.html',
    context = { 'Users': CustomUser.objects.all(), 'form': form_adduser }
  )