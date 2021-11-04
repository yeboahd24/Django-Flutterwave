from django.shortcuts import render
from django.conf import settings
from .forms import Payment
import requests
import json
from django.http import HttpResponse, JsonResponse


def home(request):
    return render(request, 'payment.html', {'public_key': settings.FLUTTERWAVE_PUBLIC_KEY})


def payment(request):

    if request.method == 'POST':
        form = Payment(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Payment successfully")

    else:
        form = Payment()
    return render(request, 'customer.html', {'form': Payment, 'public_key': settings.FLUTTERWAVE_PUBLIC_KEY})
