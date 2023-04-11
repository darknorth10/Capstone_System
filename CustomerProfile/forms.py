from django.forms import ModelForm, HiddenInput, TextInput, NumberInput, Select, DateInput
from .models import Customer


class CustomerForm(ModelForm):
    class Meta:
        model  = Customer
        fields = '__all__'
        widgets = {'last_name': TextInput(attrs={'class': 'form-control'}),'first_name': TextInput(attrs={'class': 'form-control'}), 'email': TextInput(attrs={'class': 'form-control'}), 'delivery_address': TextInput(attrs={'class': 'form-control'}),
        'sex': Select(attrs={'class': 'role-select rounded p-2', 'required': 'required'}), 'phone_number': TextInput(attrs={'class': 'form-control', 'required': 'required'}), 'permanent_address': TextInput(attrs={'class': 'form-control'}),
        'credit_eligibility':Select(attrs={'class': 'role-select rounded p-2', 'required': 'required'}), 'birthdate': DateInput(attrs={'type': 'date', 'class': 'rounded px-3 py-2', 'required': 'required'}),
         }