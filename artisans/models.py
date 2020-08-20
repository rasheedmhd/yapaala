from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField

class Photo(models.Model):
    image = CloudinaryField('artisans')

    def __str__(self):
        return self.image.url

class Artisan(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, default=None, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    work = models.CharField(max_length=100, null=True, blank=True)
    Number  = models.IntegerField()
    location = models.CharField(max_length=100, null=True, blank=True)
