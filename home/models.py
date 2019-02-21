from django.db import models

from django.urls import reverse

# Create your models here.
class House(models.Model):
    picture     = models.ImageField(upload_to='houses/%Y/%m/%d/', default=None, null=True, blank=True)
    description = models.CharField(max_length=50, default=None, null=True, blank=True)
    price       = models.IntegerField(default=None, null=True, blank=True)
    location    = models.CharField(max_length=50, default=None, null=True, blank=True)
    created     = models.DateTimeField(auto_now_add=True)
    category    = models.CharField(max_length=50, default="All", blank=True, null=True)

    def __str__(self):
        return self.description

    def amount(self):
        return "GH₵"+ str(self.price) + " /month"
'''
    def get_absolute_url(self):
        return reverse('home:home', args = [str(self.pk)])
'''
