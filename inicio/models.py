from django.db import models
from ckeditor.fields import RichTextField

class Monitor(models.Model):
    marca = models.CharField(max_length=30)
    descripcion = RichTextField()
    anio = models.IntegerField()    
    imagen = models.ImageField(upload_to='imagen', null=True, blank=True)
    
    def __str__(self):
        return f'{self.id} - {self.marca} - {self.anio} - {self.imagen}'

class Procesador(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=250)
    fecha_creacion = models.DateField()
    
    def __str__(self):
        return f'{self.marca} - {self.modelo} - {self.fecha_creacion}'
    
class Placa(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=250)
    fecha_creacion = models.DateField()
    
    def __str__(self):
        return f'{self.marca} - {self.modelo} - {self.fecha_creacion}'