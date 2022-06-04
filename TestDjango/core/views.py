from itertools import product
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
# sirve para  que los  vinculos de las  paginas sin permisos se dirija al login
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def producto(request):
    productos = Producto.objects.all()
    data = {
        'productos' : productos
    }
    return render(request, 'core/producto.html', data)

# @login_required
def despacho(request):
    return render(request, 'core/despacho.html')

@permission_required('core.add_producto')
def agregar_producto(request):
    
    data = {
        'form' :ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Creado Correctamente")
            return redirect(to = "listar_productos")
        else:
            data["form"] = formulario
    
    return render(request, 'core/producto/agregar.html', data)

@permission_required('core.add_producto')
def listar_productos(request):
    productos = Producto.objects.all()
    # crear paginas
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404
    
    
    data = {
        'entity': productos,
        'paginator' : paginator
    }
    return render(request, 'core/producto/listar.html',data)

@permission_required('core.change_producto')
def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    data = {
        'form': ProductoForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data = request.POST, instance=producto, files=request.FILES)
        if  formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to = "listar_productos")
        data['form'] = formulario
    
    return render(request, 'core/producto/modificar.html', data)

@permission_required('core.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id = id)
    producto.delete()
    messages.success(request, "Eliminado  Correctamente")
    return redirect(to = "listar_productos")

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to = "home")
        data ['form'] = formulario
        
    return render(request, 'registration/registro.html', data)