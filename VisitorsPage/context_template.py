from django.template import RequestContext
from .models import Contact

def contact(request):
    contact = Contact.objects.get(id=1)

    

    return {'contact' : contact}