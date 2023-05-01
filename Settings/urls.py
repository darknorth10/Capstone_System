from django.urls import path
from . import views

urlpatterns = [
  path('', views.settings, name='settings'),
  path('add_size/', views.addSize, name='add_size'),
  path('add_cat/', views.addCategory, name='add_cat'),
]