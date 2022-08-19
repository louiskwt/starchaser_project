from django.db import models

# Create your models here.
class SiteContent(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    links = models.JSONField(null=True)

    def __str__(self):
        return self.name
