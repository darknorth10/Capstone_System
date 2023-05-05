from django.urls import path
from . import views

urlpatterns = [
  path('', views.reports, name="reports"),
  path('user_report/', views.create_user_report, name="create_user_report"),
  path('customer_report/', views.create_customer_report, name="create_customer_report"),
  path('print_user_report/', views.print_user_report, name="print_user_report"),
  path('print_customer_report/', views.print_customer_report, name="print_customer_report"),
  path('print_sales_report/', views.create_sales_report, name="print_sales_report"),
  path('sales/all/', views.sales_transaction_all, name="all_transactions"),
  path('report_installments/', views.create_installments_report, name="create_installments_report"),
  path('installments/', views.print_installments, name="installment_report"),
  path('products_report/', views.print_product_report, name="product_report"),
  path('print_product_report/', views.create_product_report, name="print_product_report"),
  path('top_selling_products/', views.print_top_selling_report, name="top_selling_report"),
  path('print_top_selling/', views.create_top_selling_report, name="print_top_selling_report"),

] 