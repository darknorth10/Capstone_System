from django.shortcuts import render
from LoginAuthentication.models import CustomUser

# Create your views here.
def user_management(request):
  return render(request, 'UserInterface/user_management.html',
    context = { 'Users': CustomUser.objects.all(), }
  )