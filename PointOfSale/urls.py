from django.urls import path
from . import views


urlpatterns = [
  path('', views.pointofsale, name='pos'),
  path('porcelain/', views.porcelain, name='porc'),
  path('clear/', views.pos_clear, name='clear'),
]