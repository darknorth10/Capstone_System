from django.forms import ModelForm, HiddenInput
from .models import Cart

class CartQuantityForm(ModelForm):

    class Meta:
        model = Cart
        fields = ['product_id', 'quantity']
        widgets = {'product_id': HiddenInput()}