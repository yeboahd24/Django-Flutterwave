from django.forms import fields
from .models import Payment
from django import forms

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"