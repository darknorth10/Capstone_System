from django.shortcuts import render

# Create your views here.
def about_system(request):
  return render(request, 'UserInterface/about_system.html')