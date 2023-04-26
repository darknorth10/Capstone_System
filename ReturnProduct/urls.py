from django.urls import path
from . import views

urlpatterns = [
  path('', views.return_product, name='return_product'),
  path('transac/', views.search_transaction, name='transac'),


]