from django.shortcuts import render, Http404
from .models import AuditTrail
# Create your views here.
def audit_trail(request):
  if request.user.role == 'cashier':
    raise Http404('Not Found')

  audits = AuditTrail.objects.all().order_by('-timestamp')
  context = {
    'audit_table' : audits,
  }
  return render(request, 'UserInterface/audit_trail.html', context)