from .models import Product
from django import forms


class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'category', 'price', 'description', 'product_type', 'image', 'phone_number']