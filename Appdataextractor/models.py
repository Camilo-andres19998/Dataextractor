from django.db import models



class BikeStation(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    free_bikes = models.IntegerField()
    empty_slots = models.IntegerField()

    def __str__(self):
        return self.name





class Sancionario_info(models.Model):
    expediente = models.CharField(max_length=50)
    unidad_fiscalizable = models.CharField(max_length=200)
    nombre_razon_social = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    detalle = models.JSONField()
    url_detalle = models.URLField(blank=True)

    def __str__(self):
        return self.expediente

    def save(self, *args, **kwargs):
        # Validar y ajustar los valores antes de guardar
        if len(self.unidad_fiscalizable) > 200:
            self.unidad_fiscalizable = self.unidad_fiscalizable[:200]
        if len(self.nombre_razon_social) > 200:
            self.nombre_razon_social = self.nombre_razon_social[:200]
        if len(self.categoria) > 100:
            self.categoria = self.categoria[:100]
        if len(self.region) > 100:
            self.region = self.region[:100]
        if len(self.estado) > 100:
            self.estado = self.estado[:100]
        # Llamar al método save() original para guardar los datos modificados
        super().save(*args, **kwargs)

    def get_detalle_ver_detalles(self):
        return self.detalle.get('ver_detalles', '')

    def get_detalle_contenido_adicional(self):
        return self.detalle.get('contenido_adicional', {})