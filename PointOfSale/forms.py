from django import forms
from django.forms import ModelForm, HiddenInput
from .models import Cart
from SalesTransaction.models import Transaction, Item
from  django.core.exceptions import ValidationError

# For Quantity
class CartQuantityForm(ModelForm):

    class Meta:
        model = Cart
        fields = ['product_id', 'quantity']
        widgets = {'product_id': HiddenInput()}

        def clean(self):
            raw_quantity = self.cleaned_data.get('quantity')

            if raw_quantity is not None:
                if raw_quantity > 2000:
                    raise ValidationError("Exeeded maximum stocks")
                elif raw_stock < 1:
                    raise ValidationError("Stocks to be added cannot be 0")

# for Cash transactions
class CashForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['customer_name', 'contact', 'email', 'delivery_address', 'total_price', 'amount', 'change', 'transaction_type']
        widgets = {'transaction_type': HiddenInput(), 'total_price': HiddenInput(), 'change': HiddenInput()}