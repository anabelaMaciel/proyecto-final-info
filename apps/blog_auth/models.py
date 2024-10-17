from django.db import models

# Create your models here.


class Eventos(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    ubicación = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo
