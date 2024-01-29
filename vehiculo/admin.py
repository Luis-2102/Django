from django.contrib import admin
from .models import Rent
# Register your models here.

class RentAdmin(admin.ModelAdmin):
    list_display = ('fecha_renta', 'order')

admin.site.register(Rent, RentAdmin)
