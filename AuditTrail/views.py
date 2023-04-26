from django.shortcuts import render
from .models import AuditTrail
# Create your views here.
def audit_trail(request):
  audits = AuditTrail.objects.all().order_by('-timestamp')
  context = {
    'audit_table' : audits,
  }
  return render(request, 'UserInterface/audit_trail.html', context)