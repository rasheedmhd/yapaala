from django.contrib import admin

from . models import House, Category, Slider, Photo

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)

class HouseAdmin(admin.ModelAdmin):
	list_display = ['about', 'slug', 'price', 'created', 'room_count', 'picture']
	list_filter = ['room_count', 'created', 'updated', 'room_count']
	list_editable = ['price', 'room_count', 'picture']
	prepopulated_fields = {'slug': ('about',)}


admin.site.register(House, HouseAdmin)

admin.site.register(Photo)

admin.site.register(Slider)
