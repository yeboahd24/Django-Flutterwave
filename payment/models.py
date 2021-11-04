from django.db import models

class Customer(models.Model):
    amount = models.IntegerField()
    currency = models.CharField(max_length=200)
    card_number = models.IntegerField()
    cvv = models.IntegerField()
    expiry_month = models.IntegerField()
    expiry_year = models.IntegerField()
    text_ref = models.IntegerField(null=True)
    email = models.EmailField(default="dominic@gmail.com")

    def __str__(self):
        return str(self.card_number)
