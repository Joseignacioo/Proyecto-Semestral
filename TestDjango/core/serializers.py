from asyncore import read
from dataclasses import fields
from .models import Marca, Producto, Suscripcion, Categoria
from rest_framework import serializers

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class ProductoSerializers(serializers.ModelSerializer):
    marcas = MarcaSerializer(read_only=True)
    class Meta:
        model = Producto
        fields = '__all__'
        
class SuscripcionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Suscripcion
        fields = '__all__'