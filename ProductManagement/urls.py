from django.urls import path
from . import views


urlpatterns = [
  path('', views.product_management, name='product_management'),
  path('edit_product/<int:id>', views.edit_product, name='edit_prod'),
  path('add_stocks/<int:id>', views.add_stock, name='add_stock'),
  path('search_product/', views.searchProduct, name='search_product'),
  path('void_product/', views.void_product, name='void_product'),
  path('archives/', views.archive_product, name='archive_product'),

]