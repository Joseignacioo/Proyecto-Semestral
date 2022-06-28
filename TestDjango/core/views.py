from itertools import product
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Producto, Suscripcion, Despacho
from .forms import ProductoForm, CustomUserCreationForm, SuscripcionForm, DespachoForm,DespachoForm1
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
        paginator = Paginator(productos, 4)
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

def agregar_suscripcion(request):
    data = {
        'form': SuscripcionForm()
    }
    if request.method == 'POST':
        formulario = SuscripcionForm(data = request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Suscrito Correctamente")
            return redirect(to = "home")
        else:
            data["form"] = formulario
    return render(request, 'core/suscripcion/agregar.html',data)

def listar_suscripciones(request):
    suscripciones = Suscripcion.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(suscripciones, 7)
        suscripciones = paginator.page(page)
    except:
        raise Http404
    
    
    data = {
        'sub': suscripciones,
        'paginator' : paginator
    }
    return render(request, 'core/suscripcion/listar.html', data)

def eliminar_suscripcion(request, id):
    suscripcion = get_object_or_404(Suscripcion, id = id)
    suscripcion.delete()
    messages.success(request, "Eliminado  Correctamente")
    return redirect(to = "listar_suscripciones")

 
# @login_required
def despacho(request):
    return render(request, 'core/despacho.html')

def agregar_despacho(request):
    data= {
        'form' : DespachoForm()
    }
    if request.method == 'POST':
        formulario = DespachoForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto Comprado")
            return redirect(to = "home")
        else:
            data["form"] = formulario
            
    return render(request, 'core/despacho/agregar.html',data)

def listar_despacho(request):
    despacho = Despacho.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(despacho, 5)
        despacho = paginator.page(page)
    except:
        raise Http404
        
    data = {
        'entity': despacho,
        'paginator': paginator
    }
    return render(request, 'core/despacho/listar.html',data)

def listar_despacho_usuario(request):
    despacho = Despacho.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(despacho, 5)
        despacho = paginator.page(page)
    except:
        raise Http404
        
    data = {
        'entity': despacho,
        'paginator': paginator
    }
    return render(request, 'core/historial.html',data)

def modificar_despacho(request ,  id):
    despacho = get_object_or_404(Despacho, id = id)
    data = {
        'form': DespachoForm1(instance=despacho)
    }
    
    if request.method == 'POST':
        formulario = DespachoForm1(data=request.POST, instance=despacho, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listar_despacho")
        data["form"]=formulario
            
    return render(request, 'core/despacho/modificar.html',data)

def eliminar_despacho(request, id):
    consultas = get_object_or_404(Despacho, id=id)
    consultas.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listar_despacho")