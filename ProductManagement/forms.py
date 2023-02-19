from django.forms import ModelForm
from .models import Product
from django.core.exceptions import ValidationError

# from for products
class ProductForm(ModelForm):
    class Meta:
        model  = Product
        fields = '__all__'

    def clean(self):
        form_data = self.cleaned_data

        if Product.objects.filter(product_name=form_data.get('product_name')).filter(product_size=form_data.get('product_size')).exists():
             raise ValidationError("Product already exists")


# update product
class changeProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['price', 'availability', 'product_img']

# add stock quantity
class addStocksForm(ModelForm):
    class Meta:
        model = Product
        fields = ['current_stock']

    def clean(self):
        raw_stock = self.cleaned_data.get('current_stock')

        if raw_stock is not None:
            if raw_stock > 3000:
                raise ValidationError("Stocks to be added cannot exceed 3000 pieces")
            elif raw_stock < 1:
                raise ValidationError("Stocks to be added cannot be 0")
        
