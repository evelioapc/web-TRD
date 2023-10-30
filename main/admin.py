from django.contrib import admin
from .models import usuario, compra, objeto_inventario

# Register your models here.
admin.site.register(usuario)
admin.site.register(compra)
admin.site.register(objeto_inventario)