from django.contrib import admin

from . models import House, Category 

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)

class HouseAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'price', 'created', 'room_count']
	list_filter = ['room_count', 'created', 'updated', 'room_count']
	list_editable = ['price', 'room_count']
	prepopulated_fields = {'slug': ('name',)}


admin.site.register(House, HouseAdmin)