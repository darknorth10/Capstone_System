from django import forms
from django.forms import TextInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser
from django.core.exceptions import ValidationError


# Modified Registration form due to custom user model
class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = CustomUser
    fields = ("first_name", "last_name", "email", "username", "role")

class CustomUserChangeForm(UserChangeForm):

  class Meta:
    model = CustomUser
    fields = ("first_name", "password", "last_name", "email", "username", "role")

# Login Form
class LoginForm(forms.Form):
  username = forms.CharField(max_length=25, required=True)
  password = forms.CharField(max_length=25, required=True, widget=forms.PasswordInput)


class ForgotPassForm(forms.Form):
   password1 = forms.CharField(max_length=20, widget=PasswordInput(attrs={'class': 'form-control'}))
   password2 = forms.CharField(max_length=20, widget=PasswordInput(attrs={'class': 'form-control'}))
   otp = forms.CharField(max_length=6, widget=TextInput(attrs={'class': 'form-control text-center', 'maxlength': 6}))

   def clean(self):
      if self.cleaned_data.get('password2') != self.cleaned_data.get('password1'):
          raise ValidationError('Passwords do not match')
      