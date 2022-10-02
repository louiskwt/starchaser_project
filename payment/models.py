from datetime import datetime
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PaymentRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True, blank=True)
    name = models.CharField(max_length=56, default="", null=False)
    email = models.CharField(max_length=156, default="", null=False)


    def __str__(self):
        return f'Payment record for {self.user.username}'

