from django.urls import path
from . import views

urlpatterns = [
  path('', views.product_management, name='product_management')
]