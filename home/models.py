from django.db import models

from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:post_by_category', args=[self.name])


# Create your models here.
class House(models.Model):
    picture     = models.ImageField(upload_to='houses/%Y/%m/%d/', default=None, null=True, blank=True)
    name        = models.CharField(max_length=100, blank=True)
    slug        = models.SlugField(max_length=100, db_index=True)
    description = models.CharField(max_length=50, default=None, null=True, blank=True)
    price       = models.IntegerField(default=None, null=True, blank=True)
    location    = models.CharField(max_length=50, default=None, null=True, blank=True)
    room_count  = models.PositiveIntegerField()
    types       = models.CharField(max_length=100, blank=True)
    options     = models.CharField(max_length=250, blank=True)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    category    = models.ForeignKey(Category, related_name="houses", on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        index_together  = (('id', 'slug'), )

    def __str__(self):
        return self.name

    def amount(self):
        return "GH₵"+ str(self.price) + " /month"
'''
    def get_absolute_url(self):
        return reverse('home:home', args = [str(self.pk)])
'''

class Slider(models.Model):
    image = models.ImageField(upload_to='Slider_Images/%Y/%m/%d/', default=None, null=True, blank=True)
