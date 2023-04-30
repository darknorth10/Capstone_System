from django.urls import path
from . import views


urlpatterns = [
  path('', views.dashboard, name='dashboard'),
  path('change_password/<int:id>/', views.force_change_password, name='force_change_password'),
  ]