from django.forms import ModelForm, NumberInput, ModelChoiceField, TextInput
from .models import Product, TileSize, ProductCategory
from django.core.exceptions import ValidationError

# from for products
class ProductForm(ModelForm):
    category = ModelChoiceField(queryset=ProductCategory.objects.all())
    product_size = ModelChoiceField(queryset=TileSize.objects.all()) 
    class Meta:
        model  = Product
        fields = ['product_name', 'brand', 'category', 'price', 'product_size', 'current_stock', 'max_stock', 'availability', 'product_img']
        
        

    def clean(self):
        form_data = self.cleaned_data
        
        if Product.objects.filter(product_name=form_data.get('product_name')).filter(product_size=form_data.get('product_size')).exists():
             raise ValidationError("Product already exists")
        if form_data.get('max_stock') < form_data.get('current_stock') :
            raise ValidationError("Max stock must be greater than current stock")

# update product
class changeProductForm(ModelForm):
    category = ModelChoiceField(queryset=ProductCategory.objects.all())
    class Meta:
        model = Product
        fields = ['product_name', 'category', 'brand', 'price', 'availability', 'product_img', 'max_stock']


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
        

class SizeForm(ModelForm):
    class Meta:
        model = TileSize
        fields = ['size', ]
        widgets = {
            'size' : TextInput(attrs={'class': 'form-control'})
        }

class CategoryForm(ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['category', ]

        widgets = {
            'category' : TextInput(attrs={'class': 'form-control'}),
        }