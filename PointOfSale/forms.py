from django import forms
from django.forms import ModelForm, HiddenInput, TextInput, NumberInput, Select
from .models import Cart
from ProductManagement.models import Product
from SalesTransaction.models import Transaction, Item
from django.core.exceptions import ValidationError

# For Quantity
class CartQuantityForm(ModelForm):

    class Meta:
        model = Cart
        fields = ['product_id', 'quantity']
        widgets = {'product_id': HiddenInput()}

    def clean(self):
        raw_quantity = self.cleaned_data.get('quantity')
        prod_id = self.cleaned_data.get('product_id')
        product = Product.objects.get(id=prod_id)

        if raw_quantity is not None:
            if raw_quantity > product.current_stock:
                raise ValidationError("Desired quantity exceeds available stocks")

            elif raw_quantity < 1:
                raise ValidationError("Stocks to be added cannot be 0")
                    
            

# for Cash transactions
class CashForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['customer_name', 'contact', 'email', 'delivery_address', 'total_price', 'amount', 'change', 'transaction_type', 'status', 'installment']
        widgets = {'transaction_type': HiddenInput(), 'total_price': HiddenInput(), 'change': HiddenInput(), 'status': HiddenInput(), 'installment': HiddenInput(),}


class GcashForm(ModelForm):

    class Meta:
        model = Transaction
        fields = ['customer_name', 'contact', 'email', 'delivery_address', 'total_price', 'amount', 'gcash_no', 'reference_no', 'transaction_type', 'status', 'installment']
        widgets = {'transaction_type': HiddenInput(), 'total_price': HiddenInput(), 'status': HiddenInput(), 'customer_name': TextInput(attrs={'class': 'form-control'}),
        'contact': TextInput(attrs={'class': 'form-control'}), 'email': TextInput(attrs={'class': 'form-control'}), 'delivery_address': TextInput(attrs={'class': 'form-control'}),
        'amount': NumberInput(attrs={'class': 'form-control', 'step': 1, 'min': '0'}), 'gcash_no': TextInput(attrs={'class': 'form-control', 'required': 'required'}), 'reference_no': TextInput(attrs={'class': 'form-control'}), 'installment': HiddenInput(),
         }


class BankingForm(ModelForm):

    class Meta:
        model = Transaction
        fields = ['customer_name', 'contact', 'email', 'delivery_address', 'total_price', 'amount', 'banking_type', 'reference_no', 'transaction_type', 'status', 'account_name', 'bank_name', 'installment']
        widgets = {'transaction_type': HiddenInput(), 'total_price': HiddenInput(), 'status': HiddenInput(), 'customer_name': TextInput(attrs={'class': 'form-control'}),
        'contact': TextInput(attrs={'class': 'form-control'}), 'email': TextInput(attrs={'class': 'form-control'}), 'delivery_address': TextInput(attrs={'class': 'form-control'}),
        'amount': NumberInput(attrs={'class': 'form-control', 'step': 1, 'min': '0'}), 'reference_no': TextInput(attrs={'class': 'form-control'}),
        'account_name': TextInput(attrs={'class': 'form-control', 'required': 'required'}), 'bank_name': TextInput(attrs={'class': 'form-control', 'required': 'required'}), 'banking_type': Select(attrs={'class': 'role-select rounded', 'required': 'required'}), 'installment': HiddenInput(),
         }