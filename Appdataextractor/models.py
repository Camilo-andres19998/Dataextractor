from django.db import models



class BikeStation(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    free_bikes = models.IntegerField()
    empty_slots = models.IntegerField()

    def __str__(self):
        return self.name



class Informacion(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    expediente = models.CharField(max_length=20)
    unidad_fiscalizable = models.CharField(max_length=200)
    nombre_razon_social = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    detalle = models.CharField(max_length=100)

    def __str__(self):
        return self.id
