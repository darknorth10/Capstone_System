from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


# Modified Registration form due to custom user model
class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = CustomUser
    fields = ("first_name", "last_name", "email", "username", "role")

class CustomUserChangeForm(UserChangeForm):
  password = None
  class Meta:
    model = CustomUser
    fields = ("first_name", "last_name", "email", "username", "role")

# Login Form
class LoginForm(forms.Form):
  username = forms.CharField(max_length=25, required=True)
  password = forms.CharField(max_length=25, required=True, widget=forms.PasswordInput)