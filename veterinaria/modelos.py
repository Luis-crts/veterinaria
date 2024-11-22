from django.db import models
from datetime import timedelta
from datetime import date


class Publicacion(models.Model):
    CATEGORIAS = [
        ('perro', 'Perro'),
        ('gato', 'Gato'),
    ]
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.CharField(max_length=10, choices=CATEGORIAS)
    edad = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='imagenes/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultima_pipeta = models.DateField(null=True, blank=True) 
    ultima_vacuna = models.DateField()


    def __str__(self):
        return self.nombre
    
    duracion_pipeta = models.CharField(max_length=10, choices=[
        ('1', '1 mes'),
        ('3', '3 meses'),
        ('no', 'No ha sido suministrado')
    ], default='no')

    estado_vacuna = models.CharField(max_length=10, choices=[
        ('1', 'Vacuna de 1 año'),
        ('no', 'No ha sido suministrado')
    ], default='no')


    def dias_para_proxima_pipeta(self):
        proxima_pipeta = self.ultima_pipeta + timedelta(days=90)
        dias_restantes = (proxima_pipeta - date.today()).days
        return dias_restantes

    def dias_para_proxima_vacuna(self):
        proxima_vacuna = self.ultima_vacuna + timedelta(days=365)
        dias_restantes = (proxima_vacuna - date.today()).days
        return dias_restantes 
    
    