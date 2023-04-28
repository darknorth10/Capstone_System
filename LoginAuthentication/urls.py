from django.urls import path
from . import views

urlpatterns = [
  path('login/', views.login_page, name="login"),
  path('logout/', views.logout_user, name="logout"),
  path('check_email/', views.email_check, name="check_email"),
  path('forgot_password/<username>/', views.forgot_password, name="forgot_password"),
  path('resend_otp/<username>/', views.resend_otp, name="resend_otp"),
  
  ]