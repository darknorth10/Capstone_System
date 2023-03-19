from django.urls import path
from . import views


urlpatterns = [
  path('', views.pointofsale, name='pos'),
  path('add_transaction', views.add_transaction, name='cash_transaction'),
  path('add_gcash_transaction', views.add_gcash_transaction, name='gcash_transaction'),
  path('add_bank_transaction', views.add_gcash_transaction, name='bank_transaction'),
  path('porcelain/', views.porcelain, name='porc'),
  path('clear/', views.pos_clear, name='clear'),
]