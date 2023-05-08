from django.shortcuts import render, redirect
from ProductManagement.models import Product
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

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

def grout(request):
    cer_p = Product.objects.filter(category='Tile Grout')

    return render(request, 'guesttemp/grout.html',{'cer_p':cer_p})

def sanitary(request):
    cer_p = Product.objects.filter(category='Sanitary Wares')

    return render(request, 'guesttemp/sanitary_wares.html',{'cer_p':cer_p})


def send_message(request):
    if request.method == 'POST':
        a = Contact.objects.filter(id=1).exists()
        
        if a :
          a = Contact.objects.get(id=1)
          b = request.POST.get('name')
          c = request.POST.get('email')
          send_mail(
            
            f"{b}'s Feedback to Store : {c}",
              request.POST.get('message'),
              '',
              [a.email],
              fail_silently=False,
          )
          messages.success(request, 'Message has been sent.')
          return redirect('base')
          print('ok')
    print('no ok')
    return redirect('base')