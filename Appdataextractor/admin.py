from django.contrib import admin
from .models import *



class BikeStationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'latitude', 'longitude', 'free_bikes', 'empty_slots')
    list_filter = ('name',)
    search_fields = ('name',)

    ordering = ['id']  


class SancionarioAdmin(admin.ModelAdmin):
    list_display = ('expediente', 'unidad_fiscalizable', 'nombre_razon_social', 'categoria', 'region', 'estado')
    list_filter = ('categoria', 'region', 'estado')
    search_fields = ('nombre_razon_social',)

    ordering = ['expediente']


admin.site.register(BikeStation, BikeStationAdmin)
admin.site.register(Sancionario, SancionarioAdmin)
