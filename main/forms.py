from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import usuario, compra, objeto_inventario

class registrarseForm(UserCreationForm):
    pass

class agregarUsuarioForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ['nombre', 'apellidos', 'ci']

class agregarCompraForm(forms.ModelForm):
    class Meta:
        model = compra
        fields = ['producto', 'cantidad']

class agregarObjetoInventarioForm(forms.ModelForm):
    class Meta:
        model = objeto_inventario
        fields = ['nombre', 'tipo', 'cantidad']