from django.contrib import admin

from . models import Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','status', 'slug']
    list_editable = ['status']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
