from django import forms
from django.forms import ModelForm, HiddenInput, TextInput, NumberInput, Select
from .models import Cart
from ProductManagement.models import Product
from SalesTransaction.models import Transaction, Item, Installment
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
        fields = ['customer_name', 'contact', 'email', 'delivery_address', 'total_price', 'amount', 'change', 'transaction_type', 'status', 'installment', 'order_type']
        widgets = {'transaction_type': HiddenInput(), 'total_price': HiddenInput(), 'change': HiddenInput(), 'status': HiddenInput(), 'installment': HiddenInput(), 'order_type': Select(attrs={'class': 'role-select rounded', 'required': 'required'}),
        }

    def clean(self):
        paid_amount = self.cleaned_data.get('amount')
        total_price = self.cleaned_data.get('total_price')
        installment = self.cleaned_data.get('installment')

        if installment == "true" and paid_amount is not None:
            if paid_amount > total_price:
                raise ValidationError("Paid amount exceeds total price")

class GcashForm(ModelForm):

    class Meta:
        model = Transaction
        fields = ['customer_name', 'contact', 'email', 'delivery_address', 'total_price', 'amount', 'gcash_no', 'reference_no', 'transaction_type', 'status', 'installment', 'order_type']
        widgets = {'transaction_type': HiddenInput(), 'total_price': HiddenInput(), 'status': HiddenInput(), 'customer_name': TextInput(attrs={'class': 'form-control'}),
        'contact': TextInput(attrs={'class': 'form-control'}), 'email': TextInput(attrs={'class': 'form-control'}), 'delivery_address': TextInput(attrs={'class': 'form-control'}),
        'amount': NumberInput(attrs={'class': 'form-control', 'step': 1, 'min': '0'}), 'gcash_no': TextInput(attrs={'class': 'form-control', 'required': 'required'}), 'reference_no': TextInput(attrs={'class': 'form-control'}), 'installment': HiddenInput(), 'order_type': Select(attrs={'class': 'role-select rounded', 'required': 'required'}),
         }

    def clean(self):
        paid_amount = self.cleaned_data.get('amount')
        total_price = self.cleaned_data.get('total_price')
        installment = self.cleaned_data.get('installment')

        if paid_amount is not None:
            if paid_amount > total_price:
                raise ValidationError("Paid amount exceeds total price")

class BankingForm(ModelForm):

    class Meta:
        model = Transaction
        fields = ['customer_name', 'contact', 'email', 'delivery_address', 'total_price', 'amount', 'banking_type', 'reference_no', 'transaction_type', 'status', 'account_name', 'bank_name', 'installment', 'order_type']
        widgets = {'transaction_type': HiddenInput(), 'total_price': HiddenInput(), 'status': HiddenInput(), 'customer_name': TextInput(attrs={'class': 'form-control'}),
        'contact': TextInput(attrs={'class': 'form-control'}), 'email': TextInput(attrs={'class': 'form-control'}), 'delivery_address': TextInput(attrs={'class': 'form-control'}),
        'amount': NumberInput(attrs={'class': 'form-control', 'step': 1, 'min': '0'}), 'reference_no': TextInput(attrs={'class': 'form-control'}),
        'account_name': TextInput(attrs={'class': 'form-control', 'required': 'required'}), 'bank_name': TextInput(attrs={'class': 'form-control', 'required': 'required'}), 'banking_type': Select(attrs={'class': 'role-select rounded', 'required': 'required'}), 'installment': HiddenInput(), 'order_type': Select(attrs={'class': 'role-select rounded', 'required': 'required'}),
         }
    def clean(self):
        paid_amount = self.cleaned_data.get('amount')
        total_price = self.cleaned_data.get('total_price')
        installment = self.cleaned_data.get('installment')

        if paid_amount is not None:
            if paid_amount > total_price:
                raise ValidationError("Paid amount exceeds total price")
                
class BalanceForm(ModelForm):

    class Meta:
        model = Installment
        fields = ['transaction_reference', 'customer_name', 'amount_paid', 'payment_method', 'reference_no']
        widgets = {'transaction_reference': HiddenInput(), 'customer_name': HiddenInput(), 'amount_paid': NumberInput(attrs={'class': 'form-control text-center fs-5', 'step': 1, 'min': '0'}), 'payment_method': Select(attrs={'class': 'role-select w-100 fs-6 rounded border border-3'}), 'reference_no': TextInput(attrs={'class': 'form-control text-center fs-5'})}
    
    def clean(self):
        transaction_ref = self.cleaned_data.get('transaction_reference')
        payment = self.cleaned_data.get('payment_method')

        if transaction_ref is None or transaction_ref == "" or payment == "false":
            raise ValidationError("Transaction reference and payment method is required")