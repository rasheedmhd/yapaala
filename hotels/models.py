from django.db import models

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=100, default=None, blank=True, null=True)
    description = models.TextField()
    location = models.CharField(max_length=100, default=None, blank=True, null=True)
    rooms_count = models.IntegerField()
    parking_space = models.IntegerField()
    shower = models.IntegerField()
    banner = models.ImageField(upload_to='hotels', default=None, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
