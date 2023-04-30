from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='customer_profile'),
    path('edit_customer/<int:id>', views.edit_customer, name='edit_customer'),
]