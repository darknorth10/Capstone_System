from django.shortcuts import render

# Create your views here.
def reports(request):
  return render(request, 'UserInterface/reports.html')