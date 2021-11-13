import requests
from django.conf import settings

class Flutterwave:
    FLUTTERWAVE_SECRET_KEY = settings.FLUTTERWAVE_SECRET_KEY
    verification_url = 'https://api.flutterwave.com/v3/'
    
    def verify_payment(self, reference, *args, **kwargs):
        
        path = (f'/transactions/{reference}/verify')
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.FLUTTERWAVE_SECRET_KEY
        }
        
        url = self.base_url + path
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response_data = response.json()
            return response_data['status'], response_data['data']
        response_data = response.json()
        return response_data['status'], response_data['message']
        
        