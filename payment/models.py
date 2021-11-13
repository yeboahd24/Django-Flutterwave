import secrets
from django.db import models
from .flutterwave import Flutterwave
class Payment(models.Model):
    email = models.EmailField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.name)


class PaymentModel(models.Model):
    amount = models.PositiveIntegerField()
    reference = models.CharField(max_length=100)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return f"Payment {self.amount} made by {self.email}"


    def save(self, *args, **kwargs):
        while not self.reference:
            reference = secrets.token_urlsafe(50)
            similar_reference = PaymentModel.objects.filter(reference=reference)
            if not similar_reference:
                self.reference = reference
        super().save(*args, **kwargs)
        
        
    def verify_payment(self):
        flutterwave = Flutterwave()
        response = flutterwave.verify_payment(self.reference)
        if response['status'] == 'success':
            self.verified = True
            self.save()
            return True
        return False