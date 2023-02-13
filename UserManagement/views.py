from django.shortcuts import render, redirect, get_object_or_404
from LoginAuthentication.models import CustomUser
from django.contrib.auth.decorators import login_required
from LoginAuthentication.forms import CustomUserCreationForm, CustomUserChangeForm
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

  # Create a new user
  if request.method == "POST":
    form_adduser = CustomUserCreationForm(request.POST)
    errors = form_adduser.errors

    if form_adduser.is_valid():
      form_adduser.save()
      print('ok')

      # for sending response through ajax
      return JsonResponse({"success": True}, status=200)
      form_adduser = CustomUserCreationForm()
    else:
      print('error')
      return JsonResponse({"errors": errors}, status=200)
      
  return render(request, 'UserInterface/user_management.html',
    context = { 'Users': CustomUser.objects.all(), 'form': form_adduser }
  )

# for editing user information
def edit_user(request, id):
  User = CustomUser.objects.get(id=id)
  # creaates form in the instance of objecct given by user id
  obj = get_object_or_404(CustomUser, id = id)
  
  form_update = CustomUserChangeForm(request.POST or None, instance = obj)
  form_update.fields['username'].widget.attrs.update({'readonly': 'true'})
  errors = form_update.errors
  if form_update.is_valid():
    form_update.save()
    return JsonResponse({"success": True}, status=200)
    
  else:
    print(form_update.errors)

  return render(request, 'UserInterface/edituser.html', context = { 'Users': User, 'form': form_update})


# update user status (active or inactive)
def update_status_inactive(request):

  if request.method == "POST":
    # get user id sent via ajax
    update_id = request.POST['id']
    User_status = CustomUser.objects.get(id=update_id)
    # activates user status
    if not User_status.is_active:
      User_status.is_active =  True
      User_status.save()
      return JsonResponse({"success": "activated"}, status=200)
    # deactivates user status
    else:
      User_status.is_active =  False
      User_status.save() 
      return JsonResponse({"success": "deactivated"}, status=200)



