from random import randrange
from django import forms
from .models import Customer

class Payment(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['text_ref']

    def save(self, *args, **kwargs):
        self.fields['text_ref'] = randrange(1, 10000)
        return super().save(*args, **kwargs)