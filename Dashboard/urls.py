from django.urls import path
from . import views
  # TODO: write code...

urlpatterns = [
  path('', views.dashboard, name='dashboard'),
  ]