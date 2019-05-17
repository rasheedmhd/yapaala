from django.contrib import admin

# Register your models here.
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name', 'house_address', 'Number', 'Accepted')
    search_fields = ('name', 'house_address', 'location')
    list_filter = ('name', 'Date', 'location', 'network')


admin.site.register(Payment, PaymentAdmin)
