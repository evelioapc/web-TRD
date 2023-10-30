from django.db import models

# Create your models here.

class quejaSugerencia(models.Model):
    ciUsuario = models.CharField(max_length=11)
    quejaSugerencia= models.CharField(max_length=400)
    resuelta= models.BooleanField()

class usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=60)
    ci = models.CharField(max_length=11)

    def __str__(self):
        return self.nombre
