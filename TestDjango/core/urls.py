from django.urls import path
from .views import eliminar_producto, home, producto, despacho, agregar_producto, listar_productos,\
                    modificar_producto, eliminar_producto, registro, agregar_suscripcion, listar_suscripciones, eliminar_suscripcion

urlpatterns = [
    path('', home, name="home"),
    path('producto/', producto, name="producto"),
    path('despacho/', despacho, name="despacho"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-productos/', listar_productos, name= "listar_productos"),
    path('modificar-producto/<id>/', modificar_producto , name="modificar_producto"),
    path('eliminar-producto/<id>/' , eliminar_producto, name="eliminar_producto"),
    path('registro/', registro, name="registro"),
    path('suscripcion/',agregar_suscripcion, name='agregar_suscripcion'),
    path('listar-suscripciones/',listar_suscripciones,name='listar_suscripciones'),
    path('eliminar-suscripciones/<id>/',eliminar_suscripcion, name='eliminar_suscripciones'),
]