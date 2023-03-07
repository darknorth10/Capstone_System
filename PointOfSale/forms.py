from django.forms import ModelForm, HiddenInput
from .models import Cart
from  django.core.exceptions import ValidationError

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