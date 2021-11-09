from django.shortcuts import render,redirect
from django.conf import settings
import requests
import json
from django.http import HttpResponse, JsonResponse





def payment_view(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        name = request.POST.get('name')
        currency = request.POST.get('currency')
        public_key = settings.FLUTTERWAVE_PUBLIC_KEY
        secret_key = settings.FLUTTERWAVE_SECRET_KEY
        url = 'https://api.ravepay.co/flwv3-pug/getpaidx/api/v2/hosted/pay'
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            "amount": amount,
            "customer_email": email,
            "customer_phone": phone,
            "customer_firstname": name,
            "customer_lastname": name,
            "currency": currency,
            "country": "NG",
            "redirect_url": "https://www.google.com/",
            "payment_method": "both",
            "public_key": public_key,
            "secret_key": secret_key
        }
        response = requests.post(url, headers=headers, data=json.dumps(data))
        return JsonResponse(response.json())
    else:
        return render(request, 'charge.html')


def payment_link(request):
   return redirect('https://ravesandbox.flutterwave.com/pay/hmzofhfo7dvf')


def make_payment(request):
    return render(request, 'payment.html', {'public_key': settings.FLUTTERWAVE_PUBLIC_KEY})