from django.db import models

class Member(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre

class Trainer(models.Model):
    nombre = models.CharField(max_length=100)
    experiencia = models.CharField(max_length=100)
    tarifa = models.DecimalField(max_digits=6, decimal_places=2)

class Class(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    entrenador = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    miembros = models.ManyToManyField(Member)

