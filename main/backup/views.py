from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import registrarseForm, agregarUsuarioForm
from .models import usuario

# Create your views here.
@login_required
def gestionarUsuario(request):
    usuarios = usuario.objects.order_by('nombre')
    context = {'lista_usuarios' : usuarios}
    return render(request, 'gestionarUsuario.html', context)

def paginaPrincipal (request):
    return render (request, 'paginaPrincipal.html')

def register (request):
    data = {
        'form' : registrarseForm ()
    }

    if request.method == 'POST':
        user_creation_form = registrarseForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            return redirect('paginaPrincipal')

    return render (request, 'registration/register.html', data)

def agregarUsuario (request):
    if request.method == 'POST':
        form = agregarUsuarioForm (request.POST)
        
        if form.is_valid():
            nuevoElemento = form.save()
            return redirect('gestionarUsuario')

    else:
        form = agregarUsuarioForm()

    return render (request, 'agregarUsuario.html', {'form' : form})

def eliminarUsuario(request, idUsuario):
    u = usuario.objects.get(id = idUsuario)
    u.delete()
    return redirect('gestionarUsuario')

#Para modificar usuario
def verUsuario(request, idUsuario):
    u = get_object_or_404(usuario, id = idUsuario)
    form = agregarUsuarioForm(instance=u)
    context = {'form':form, 'usuario':u}
    return render(request, 'modificarUsuario.html', context)

def guardarUsuario(request, idUsuario):
    u = get_object_or_404(usuario, id=idUsuario)
    form = agregarUsuarioForm(request.POST, instance=u)
    if form.is_valid():
        form.save()
        return redirect('gestionarUsuario')

    return render(request, 'modificarUsuario.html', {'form': form})