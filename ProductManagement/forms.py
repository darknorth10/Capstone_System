from django.forms import ModelForm
from .models import Product

# from for products
class ProductForm(ModelForm):
    class Meta:
        model  = Product
        fields = '__all__'