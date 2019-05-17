from django import forms

from .models import Payment

class TransactionForm(forms.Form):

    class Meta:
        model = Payment()
        fields = (
        'house_address'
        'amount_sent',
        'Network',
        'Date',
        'Description',
        'Transaction_Details',
        )
