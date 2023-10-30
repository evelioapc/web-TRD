from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=60)
    ci = models.CharField(max_length=11)

    def __str__(self):
        return self.nombre

class compra(models.Model):
    producto = models.CharField(max_length = 40)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.producto

class objeto_inventario(models.Model):
    nombre = models.CharField(max_length=40)
    tipo = models.CharField(max_length=40)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre