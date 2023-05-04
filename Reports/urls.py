from django.urls import path
from . import views

urlpatterns = [
  path('', views.reports, name="reports"),
  path('user_report/', views.create_user_report, name="create_user_report"),
  path('customer_report/', views.create_customer_report, name="create_customer_report"),
  path('print_user_report/', views.print_user_report, name="print_user_report"),
  path('print_customer_report/', views.print_customer_report, name="print_customer_report"),

]