from django.db import models

from django.urls import reverse


class Blog(models.Model):
    STATUS_CHOICES = {
    ('DRAFT', 'Draft'),
    ('PUBLISHED', 'Published')
    }
    title = models.CharField(max_length=120)
    body  = models.TextField()
    writer = models.CharField(max_length=50)
    blog_image = models.ImageField(upload_to='blogging/post/%Y/%m/%d/', blank=True, null=True)
    publish = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug    = models.SlugField()
    status  = models.CharField(max_length=20, choices=STATUS_CHOICES, default="DRAFT")

    class Meta:
        ordering = ('-publish',)

    def get_absolute_url(self):
        return reverse('blog:blog_home', args = [self.slug])
