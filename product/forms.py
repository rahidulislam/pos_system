from django import forms
from product.models import Category, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('parent', 'name', 'code', 'image', 'is_active')


class ProductFrom(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('slug',)
