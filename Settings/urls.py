from django.urls import path
from . import views

urlpatterns = [
  path('', views.settings, name='settings'),
  path('add_size/', views.addSize, name='add_size'),
  path('add_cat/', views.addCategory, name='add_cat'),
  path('up_p/', views.update_phone, name='up_p'),
  path('ue_p/', views.update_email, name='ue_p'),
  path('ul_p/', views.update_location, name='ul_p'),
]