from django.contrib import admin
from .models import Marca, Producto
from .forms import ProductoForm

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    form = ProductoForm

admin.site.register(Marca)
admin.site.register(Producto)

