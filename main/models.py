from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='avatars')

    def __str__(self):
        return f'{self.user.username} Profile'

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
    
    def __str__(self):
        return f"{self.user} - {self.imagen}"