# Importa el módulo settings de Django
from django.conf import settings
import os
import django
# Define una función que configurará la base de datos de prueba
def pytest_configure():
    settings.DEBUG = False
    settings.DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    }