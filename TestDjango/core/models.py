from cProfile import run
from distutils.command.upload import upload
import email

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
    stock = models.IntegerField(default=0, verbose_name="Stock")
    
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    idCategoria = models.CharField(max_length=50, verbose_name="Nombre de la Marca | Categoria")
    
    def __str__(self):
        return self.idCategoria
    
class Suscripcion(models.Model):
    rut = models.CharField(max_length=9)
    nombre = models.CharField(max_length=50)
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self): 
        return self.rut

class Estado(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Estado del Despacho")
    
    def __str__(self):
        return self.nombre

class Despacho(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    telefono = models.IntegerField()
    estado = models.ForeignKey(Estado,null=True,blank=True, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.nombre