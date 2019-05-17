from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Artisan(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    work = models.CharField(max_length=100, null=True, blank=True)
    Number  = models.IntegerField()
    location = models.CharField(max_length=100, null=True, blank=True)
