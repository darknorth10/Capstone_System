from django.shortcuts import render

# Create your views here.
def user_management(request):
  return render(request, 'UserInterface/user_management.html')