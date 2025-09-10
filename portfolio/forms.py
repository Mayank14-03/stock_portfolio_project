from django import forms
from .models import Holding

class HoldingForm(forms.ModelForm):
    class Meta:
        model = Holding
        fields = ['stock_symbol', 'quantity', 'purchase_price']
        widgets = {
            'stock_symbol': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter stock symbol e.g. TCS.NS'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'purchase_price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
