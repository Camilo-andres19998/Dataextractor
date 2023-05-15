from django.db import models

from django.db import models

class BikeStation(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    free_bikes = models.IntegerField()
    empty_slots = models.IntegerField()

    def __str__(self):
        return self.name
