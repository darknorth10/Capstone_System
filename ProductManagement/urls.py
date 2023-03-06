from django.urls import path
from . import views


urlpatterns = [
  path('', views.product_management, name='product_management'),
  path('edit_product/<int:id>', views.edit_product, name='edit_prod'),
  path('add_stocks/<int:id>', views.add_stock, name='add_stock'),
] 