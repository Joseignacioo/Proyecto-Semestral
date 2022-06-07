from dataclasses import fields
import email
from email.mime import image
from tkinter import Widget
from django import forms
from .models import Producto, Suscripcion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidator
from django.forms import ValidationError

class ProductoForm(forms.ModelForm):
    
    # validaciones
    nombre =forms.CharField(min_length=3,max_length=50)
    precio = forms.IntegerField(min_value=1, max_value=100000)
    imagen = forms.ImageField(required=False, validators=[MaxSizeFileValidator(max_file_size=2)])
    
    class Meta:
        model = Producto
        fields = '__all__'
        
        Widgets = {
            "fecha_fabricacion": forms.SelectDateWidget()
        }
        
class CustomUserCreationForm(UserCreationForm):
    
    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Producto.objects.filter(nombre__iexcat = nombre).exists()

        if  existe:
            raise ValidationError("Este nombre ya existe")
        return nombre
    
    class Meta:
        model = User
        fields = ['username',"first_name","last_name","email","password1", "password2"]
        
class SuscripcionForm(forms.ModelForm):
    
    class Meta:
        model = Suscripcion
        fields = '__all__'