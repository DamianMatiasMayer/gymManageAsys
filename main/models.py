from django.db import models

class Member(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre

class Trainer(models.Model):
    nombre = models.CharField(max_length=100)
    experiencia_anios = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.experiencia_anios} years of experience"

class Class(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    entrenador = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    miembros = models.ManyToManyField(Member)

