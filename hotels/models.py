from django.db import models

from cloudinary.models import CloudinaryField

class Photo(models.Model):
    image = CloudinaryField('hotels')

    def __str__(self):
        return self.image.url

class Manager(models.Model):
    first_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    second_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, default=None, null=True, blank=True)
    telephone = models.IntegerField(default=None, blank=True, null=True)
    email = models.EmailField(default=None, blank=True, null=True)
    website = models.CharField(max_length=150, default=None, blank=True, null=True)
    about = models.CharField(max_length=150, default=None, blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.second_name



# Create your models here.
class Hotel(models.Model):
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default=None, blank=True, null=True)
    description = models.TextField()
    location = models.CharField(max_length=100, default=None, blank=True, null=True)
    rooms = models.IntegerField()
    parking = models.IntegerField()
    rate = models.IntegerField()
    banner = models.ForeignKey(Photo, on_delete=models.CASCADE, default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
