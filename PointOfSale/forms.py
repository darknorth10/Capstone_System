from django import forms
from django.forms import ModelForm, HiddenInput
from .models import Cart
from ProductManagement.models import Product
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
        fields = ['customer_name', 'contact', 'email', 'delivery_address', 'total_price', 'amount', 'change', 'transaction_type']
        widgets = {'transaction_type': HiddenInput(), 'total_price': HiddenInput(), 'change': HiddenInput()}