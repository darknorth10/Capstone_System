from django.forms import ModelForm, HiddenInput, TextInput, NumberInput, Select, Textarea
from .models import ReturnItem
from django.core.exceptions import ValidationError


class ReturnItemForm(ModelForm):

    class Meta:
        model = ReturnItem
        fields = ['name', 'quantity', 'size', 'orig_quantity', 'transact_no', 'description']
        widgets = {'transact_no': HiddenInput(), 'orig_quantity': HiddenInput(), 'size': HiddenInput(), 'name': HiddenInput(), 'quantity': NumberInput(attrs={'class': 'form-control', 'step': '1', 'min' : '1'}),
        'description': Textarea(attrs={'class': 'form-control', 'rows': '3',})
        }
    
    def clean(self):
        quantity = self.cleaned_data.get('quantity')
        orig_quantity = self.cleaned_data.get('orig_quantity')
        tnum = self.cleaned_data.get('transact_no')
        name = self.cleaned_data.get('name')

        checkItem = ReturnItem.objects.filter(transact_no=tnum).filter(name=name)
        quantity_sum = 0

        for item in checkItem:
            quantity_sum += item.quantity

        if quantity > orig_quantity and quantity is not None:
                raise ValidationError("You exceeded the quantity limit")
        
        elif checkItem and quantity_sum >= orig_quantity:
                raise ValidationError("You have already returned this item.")
