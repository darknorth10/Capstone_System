from django.shortcuts import render
from ProductManagement.models import Product
from .models import Contact
# Create your views here.

# Create your views here.
def base(request):
    posts = Product.objects.all()
    contact = Contact.objects.get(id=1)
    return render(request,'guesttemp/all.html', {'posts':posts, 'contact':contact})   

def guest_up(request):
    #if request.method == 'GET':     
     posts = Product.objects.filter(category='Adhesive')
     return render(request, 'guesttemp/Adhesive.html',{'posts':posts})

def porcelain_up(request):
     pos_p = Product.objects.filter(category='Porcelain Tiles')
     return render(request, 'guesttemp/Porcelaintile.html',{'pos_p':pos_p}) 

def ceramic_up(request):
    cer_p = Product.objects.filter(category='Ceramic Tiles')

    return render(request, 'guesttemp/ceramic.html',{'cer_p':cer_p})
