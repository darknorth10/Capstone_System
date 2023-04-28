from django.urls import path
from . import views

urlpatterns = [
  path('login/', views.login_page, name="login"),
  path('logout/', views.logout_user, name="logout"),
  path('forgot_password/<int:id>/', views.forgot_password, name="forgot_password"),
  
  ]