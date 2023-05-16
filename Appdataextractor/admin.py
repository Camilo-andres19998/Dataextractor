from django.contrib import admin
from .models import BikeStation

class BikeStationAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'free_bikes', 'empty_slots')
    list_filter = ('name',)  
    search_fields = ('name',)  

admin.site.register(BikeStation, BikeStationAdmin)
