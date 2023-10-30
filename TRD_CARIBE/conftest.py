# Importa el módulo settings de Django
from django.conf import settings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
# Define una función que configurará la base de datos de prueba
def pytest_configure():
    settings.DEBUG = False
    settings.DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR /'dbTEST.sqlite3',
        }
    }