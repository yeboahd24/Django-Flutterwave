from os import name
from django.db import models

class Payment(models.Model):
    email = models.EmailField(max_length=200)
    name  = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return str(self.name)