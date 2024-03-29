from django.db import models

from django.urls import reverse

from cloudinary.models import CloudinaryField

class Photo(models.Model):
    image = CloudinaryField('houses')

    def __str__(self):
        return self.image.url

class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "Town"
        verbose_name_plural = "Towns"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:post_by_category', args=[self.name])


# Create your models here.
class House(models.Model):
    picture     = models.ForeignKey(Photo, on_delete=models.CASCADE, default=None, null=True, blank=True)
    about       = models.CharField(max_length=100, blank=True)
    slug        = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(default=None, null=True, blank=True)
    price       = models.IntegerField(default=None, null=True, blank=True)
    location    = models.CharField(max_length=50, default=None, null=True, blank=True)
    room_count  = models.PositiveIntegerField()
    types       = models.CharField(max_length=100, blank=True)
    options     = models.CharField(max_length=250, blank=True)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    category    = models.ForeignKey(Category, related_name="houses", on_delete=models.CASCADE)

    class Meta:
        ordering = ('about',)
        index_together  = (('id', 'slug'), )

    def __str__(self):
        return self.about

    def amount(self):
        return "GH₵ "+ str(self.price) + "/month"

'''
    def get_absolute_url(self):
        return reverse('home:home', args = [str(self.pk)])
'''
