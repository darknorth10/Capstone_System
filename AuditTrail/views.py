from django.shortcuts import render

# Create your views here.
def audit_trail(request):
  return render(request, 'UserInterface/audit_trail.html')