from django.shortcuts import render, redirect
from LoginAuthentication.models import CustomUser
from django.contrib.auth.decorators import login_required
from LoginAuthentication.forms import CustomUserCreationForm
from django.http import JsonResponse
# Create your views here.
@login_required(login_url='login')
def user_management(request):

  #instance of user creation form for creating user
  form_adduser = CustomUserCreationForm()

  #for addingg required attribute on to the inpu fields that are not required by default
  form_adduser.fields['first_name'].widget.attrs.update({'required': True})
  form_adduser.fields['last_name'].widget.attrs.update({'required': True})
  form_adduser.fields['email'].widget.attrs.update({'required': True})
  form_adduser.fields['password2'].widget.attrs.update({'minlength': '8'})

  if request.method == "POST":
    form_adduser = CustomUserCreationForm(request.POST)
    errors = form_adduser.errors

    if form_adduser.is_valid():
      form_adduser.save()
      print('ok')
      return JsonResponse({"success": True}, status=200)
      form_adduser = CustomUserCreationForm()
    else:
      print('error')
      return JsonResponse({"errors": errors}, status=200)
      
  return render(request, 'UserInterface/user_management.html',
    context = { 'Users': CustomUser.objects.all(), 'form': form_adduser }
  )