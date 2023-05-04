from django.template import RequestContext
from .models import Notification

def notification(request):
    notif = Notification.objects.all().order_by('-pk')

    notifNum = Notification.objects.filter(status='pending').count()

    return {'notifs' : notif, 'num' : notifNum}