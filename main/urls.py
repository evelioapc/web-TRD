from django.urls import path
from . import views

urlpatterns = [
    path('', views.paginaPrincipal, name='paginaPrincipal'),
    path('gestionarUsuario/', views.gestionarUsuario, name = 'gestionarUsuario'),
    path('register/', views.register, name = 'register'),
    #para Gestionar usuarios
    path('agregarUsuario/', views.agregarUsuario, name='agregarUsuario'),
    path('eliminarUsuario/<int:idUsuario>', views.eliminarUsuario, name='eliminarUsuario'),
    path('verUsuario/<int:idUsuario>',views.verUsuario, name='verUsuario'),
    path('guardarUsuario/<int:idUsuario>', views.guardarUsuario, name='guardarUsuario'),
    #para administrar Compra
    path('administrarCompra/', views.administrarCompra, name='administrarCompra'),
    path('eliminarCompra/<int:idCompra>', views.eliminarCompra, name = 'eliminarCompra'),
    path('agregarCompra/', views.agregarCompra, name = 'agregarCompra'),
    #para Administrar Inventario
    path('administrarInventario', views.administrarInventario, name = 'administrarInventario'),
    path('eliminarObjetoInventario/<int:idObjeto>', views.eliminarObjetoInventario, name = 'eliminarObjetoInventario'),
    path('agregarObjetoInventario', views.agregarObjetoInventario, name = 'agregarObjetoInventario'),
]