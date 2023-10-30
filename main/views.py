from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import registrarseForm, agregarUsuarioForm, agregarCompraForm, agregarObjetoInventarioForm
from .models import usuario, compra, objeto_inventario

# Create your views here.
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

# Para Gestionar usuario  ########################

@login_required
def gestionarUsuario(request):
    usuarios = usuario.objects.order_by('nombre')
    context = {'lista_usuarios' : usuarios}
    return render(request, 'gestionarUsuario.html', context)

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

#   Para modificar usuario   #########
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
###################################


#   Para Las compras  ############
@login_required
def administrarCompra(request):
    compras = compra.objects.order_by('producto')
    context = {'lista_compras' : compras}
    return render (request, 'administrarCompra.html', context)

def eliminarCompra(request, idCompra):
    c = compra.objects.get(id = idCompra)
    c.delete()
    return redirect('administrarCompra')

def agregarCompra (request):
    if request.method == 'POST':
        form = agregarCompraForm (request.POST)
        
        if form.is_valid():
            nuevoElemento = form.save()
            return redirect('administrarCompra')

    else:
        form = agregarCompraForm()

    return render (request, 'agregarCompra.html', {'form' : form})
#########################

#  Para Administrar Inventario  ######################
@login_required
def administrarInventario(request):
    objetos = objeto_inventario.objects.order_by('nombre')
    context = {'lista_objetos' : objetos}
    return render(request, 'administrarInventario.html', context)

def eliminarObjetoInventario(request, idObjeto):
    o = objeto_inventario.objects.get(id = idObjeto)
    o.delete()
    return redirect('administrarInventario')

def agregarObjetoInventario (request):
    if request.method == 'POST':
        form = agregarObjetoInventarioForm (request.POST)
        
        if form.is_valid():
            nuevoElemento = form.save()
            return redirect('administrarInventario')

    else:
        form = agregarObjetoInventarioForm()

    return render (request, 'agregarObjetoInventario.html', {'form' : form})