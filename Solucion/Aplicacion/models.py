from django.db import models

# Create your models here.
class Slider(models.Model):
    identif = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='fotos',null=True)

    def __str__(self):
        return self.nombre

class Galeria(models.Model):
    identif = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='fotos',null=True)

    def __str__(self):
        return self.nombre

class MisionyVision(models.Model):
    identif = models.CharField(max_length=50,primary_key=True)
    mision = models.TextField()
    vision = models.TextField()
    def __str__(self):
        return self.identif

class Productos(models.Model):
    nombre = models.CharField(max_length=120,primary_key=True)
    precio = models.IntegerField()
    descripcion = models.TextField()
    stock = models.IntegerField()
    def __str__(self):
        return self.nombre