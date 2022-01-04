from sell.models import Sell
from django import forms


class SellForm(forms.ModelForm):
    class Meta:
        model = Sell
        fields = "__all__"
        widgets = {
            'sell_date': forms.DateInput(attrs={'type': 'date'}),
            'sell_note': forms.Textarea(attrs={'rows': '3'})
        }
