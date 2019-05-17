from django.db import models

class Realtor(models.Model):
    first_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    second_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    photo = models.ImageField(upload_to='realtors/%Y/%m/%d/', default=None, blank=True, null=True)
    telephone = models.IntegerField(default=None, blank=True, null=True)
    email = models.EmailField(default=None, blank=True, null=True)
    website = models.CharField(max_length=150, default=None, blank=True, null=True)
    about = models.CharField(max_length=150, default=None, blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.second_name



# Create your models here.
class Hotel(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
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
