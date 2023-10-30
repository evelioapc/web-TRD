from django.test import TestCase
from django.urls import reverse
from .models import usuario, compra
import pytest

@pytest.mark.django_db
def test_create_usuario():
    # Creamos un objeto Usuario
    newUsuario = usuario.objects.create(nombre = 'Prueba', apellidos = 'Apellidos Prueba', ci = '00112968003')

    # Verificamos que el objeto se haya creado exitosamente
    assert newUsuario.pk is not None

    # Verificamos que los campos sean los correctos
    assert newUsuario.nombre == 'Prueba'
    assert newUsuario.apellidos == 'Apellidos Prueba'
    assert newUsuario.ci == '00112968003'

class MyViewTestCase(TestCase):

    def test_view_PaginaPrincipal(self):
        # Obtiene la URL correspondiente a la vista
        url = reverse('paginaPrincipal')

        # Realiza una solicitud GET a la vista
        response = self.client.get(url)

        # Verifica que la respuesta tenga un código de estado 200
        self.assertEqual(response.status_code, 200)

@pytest.mark.django_db
def test_create_Compra():
    # Creamos un objeto Usuario
    newCompra = compra.objects.create(producto = 'Plancha', cantidad = 1)

    # Verificamos que el objeto se haya creado exitosamente
    assert newCompra.pk is not None

    # Verificamos que los campos sean los correctos
    assert newCompra.producto == 'Plancha'
    assert newCompra.cantidad == 1
    

