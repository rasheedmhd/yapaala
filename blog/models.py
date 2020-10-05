from django.db import models

from django.urls import reverse

from cloudinary.models import CloudinaryField


class Photo(models.Model):
    image = CloudinaryField('lands')

    def __str__(self):
        return self.image.url

class Land(models.Model):
    title = models.CharField(max_length=120)
    price = models.CharField(max_length=12, default=None, null=True, blank=True)
    body  = models.TextField()
    more_infor = models.TextField()
    seller = models.CharField(max_length=50)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, default=None, null=True, blank=True)
    publish = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug    = models.SlugField()

    class Meta:
        ordering = ('-publish',)

    def amount(self):
        return "GH₵ "+ str(self.price)

    def get_absolute_url(self):
        return reverse('lands:lands', args = [self.slug])
