from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import usuario, quejaSugerencia

class registrarseForm(UserCreationForm):
    pass

class agregarUsuarioForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ['nombre', 'apellidos', 'ci']