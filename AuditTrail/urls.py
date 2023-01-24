from django.urls import path
from . import views

urlpatterns = [
  path('', views.audit_trail, name='audit_trail'),
]