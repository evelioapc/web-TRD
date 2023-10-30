from django.urls import path
from . import views

urlpatterns = [
    path('', views.paginaPrincipal, name='paginaPrincipal'),
    path('gestionarUsuario/', views.gestionarUsuario, name = 'gestionarUsuario'),
    path('register/', views.register, name = 'register'),
    path('agregarUsuario/', views.agregarUsuario, name='agregarUsuario'),
    path('eliminarUsuario/<int:idUsuario>', views.eliminarUsuario, name='eliminarUsuario'),
    #para modificar usuarios
    path('verUsuario/<int:idUsuario>',views.verUsuario, name='verUsuario'),
    path('guardarUsuario/<int:idUsuario>', views.guardarUsuario, name='guardarUsuario'),
]
