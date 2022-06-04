from distutils.command.upload import upload
from pyexpat import model
from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre de la Marca | Categoria")

def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    fecha_fabricacion = models.DateField()
    imagen = models.ImageField(upload_to = "productos" , null=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre