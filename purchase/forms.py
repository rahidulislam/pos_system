from django import forms
from purchase.models import Purchase


class PurchaseProductForm(forms.Form):
    pass


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
            'purchase_note': forms.Textarea(attrs={'rows': '3'})
        }
