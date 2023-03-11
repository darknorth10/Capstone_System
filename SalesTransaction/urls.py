from django.urls import path
from . import views

urlpatterns = [
  path('', views.sales_transaction, name='sales_transaction'),
  path('<int:id>/', views.view_detailed, name='detailed'),
  path('payment_info/', views.payment_info, name='payment_info'),
  
]