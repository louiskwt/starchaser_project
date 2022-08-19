from email.policy import default
from django.db import models

# Create your models here.
class SiteContent(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.name
