from django.contrib import admin
from .models import Marca, Producto, Categoria, Suscripcion
from .forms import ProductoForm

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    form = ProductoForm

admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Suscripcion)

