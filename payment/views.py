from django.shortcuts import render
from django.conf import settings

def home(request):
    return render(request, 'payment.html', {'public_key': settings.FLUTTERWAVE_PUBLIC_KEY})