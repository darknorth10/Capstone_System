from django.forms import ModelForm, EmailInput, TextInput
from .models import Contact

class PhoneForm(ModelForm):
    class Meta:
        model = Contact

        fields = ['phone', ]
        widgets = {'phone': TextInput(attrs={'class': 'form-control'})}


class EmailForm(ModelForm):
    class Meta:
        model = Contact

        fields = ['email', ]
        widgets = {'email': EmailInput(attrs={'class': 'form-control'})}

class LocationForm(ModelForm):
    class Meta:
        model = Contact

        fields = ['location', ]
        widgets = {'location': TextInput(attrs={'class': 'form-control'})}
