from django import forms
from product.models import Category

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ('parent','name', 'code', 'image', 'is_active')
