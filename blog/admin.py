from django.contrib import admin

from . models import Land, Photo
# Register your models here.

class LandAdmin(admin.ModelAdmin):
    list_display = ['title','seller', 'slug']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Land, LandAdmin)

admin.site.register(Photo)