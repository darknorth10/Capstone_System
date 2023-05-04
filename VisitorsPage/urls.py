from django.urls import path
from .import views as guest_views
#from mainweb import views as gallery #import the views of mainweb into the  guestpageviews
""" from django.conf.urls.static import static
from django.conf import settings
#create urls here """
urlpatterns = [
      path('', guest_views.base, name='base'),
#      path('All category/',guest_views.all,name='all_up'),
      path('Adhesive/',guest_views.guest_up,name='guest_up'),
      path('Porcelain/',guest_views.porcelain_up,name='por_up'),
      path('Ceramic/',guest_views.ceramic_up,name='cer_up'),
   
      



      
      #path('register',guest_views.register, name='register'),
]