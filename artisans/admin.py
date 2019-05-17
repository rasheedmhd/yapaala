from django.contrib import admin

# Register your models here.
from .models import Artisan

class ArtisanAdmin(admin.ModelAdmin):
    list_display = ('name', 'work', 'Number', 'location')
    search_fields = ('name', 'work', 'location')
    list_filter = ('work', 'location')

admin.site.register(Artisan, ArtisanAdmin)
