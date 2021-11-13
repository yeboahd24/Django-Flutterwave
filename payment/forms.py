from django.forms import fields
from .models import Payment, PaymentModel
from django import forms

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"
        
        
class VerifyPaymentForm(forms.ModelForm):
    class Meta:
        model = PaymentModel
        fields = ('email', 'amount',)