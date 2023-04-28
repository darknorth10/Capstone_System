from django.forms import Form, PasswordInput, HiddenInput, TextInput, CharField
from LoginAuthentication.models import CustomUser
from LoginAuthentication.forms import CustomUserChangeForm
from django.core.exceptions import ValidationError


class ResetPassword(Form):
    password1 = CharField(max_length=20, widget=PasswordInput(attrs={'class': 'form-control'}))
    password2 = CharField(max_length=20, widget=PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        if self.cleaned_data.get('password2') != self.cleaned_data.get('password1'):
            raise ValidationError('Passwords do not match')

    