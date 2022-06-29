from django.db import router
from django.urls import path, include
from .views import SuscripcionViewset,ProductoViewset, eliminar_producto, home, producto, despacho, agregar_producto, listar_productos,\
                    modificar_producto, eliminar_producto, registro, agregar_suscripcion, listar_suscripciones, eliminar_suscripcion,\
                        agregar_despacho,listar_despacho,listar_despacho_usuario,modificar_despacho,eliminar_despacho
from rest_framework import routers
router = routers.DefaultRouter()
router.register('producto', ProductoViewset)
router.register('Suscripcion',SuscripcionViewset)


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
    path('agregar-despacho/',agregar_despacho,name="agregar_despacho"),
    path('listar-despacho/',listar_despacho,name="listar_despacho"),
    path('historial/',listar_despacho_usuario,name="listar_despacho_usuario"),
    path('modificar_despacho/<id>/',modificar_despacho,name="modificar_despacho"),
    path('eliminar-despacho/<id>/',eliminar_despacho,name="eliminar_despacho"),
    path('api/',include(router.urls)),
]