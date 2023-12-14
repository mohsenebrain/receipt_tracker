# receipts/forms.py
from django import forms
from .models import Receipt

class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ['name', 'date_purchase', 'item_list', 'total_amount']
