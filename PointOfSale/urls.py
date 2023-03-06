from django.urls import path
from . import views


urlpatterns = [
  path('', views.pointofsale, name='pos'),
  path('', views.porcelain, name='porc'),
]