from django.urls import path
from . import views

urlpatterns = [
  path('', views.sales_transaction, name='sales_transaction' ),
  path('payment_info/', views.payment_info, name='payment_info' ),
  path('items_transaction/<int:id>/', views.items_transaction, name='item_info' ),
  
]