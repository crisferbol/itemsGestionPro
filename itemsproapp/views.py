from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models.cliente import cliente
from .models import producto
from .models import solicitud
from .forms import clienteForm, productoForm, solicitudForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_admin')  
        else:
            messages.error(request, 'Correo electrónico o contraseña incorrectos')
    
    return render(request, 'login.html')

def home(request):
    return render(request, 'registration/login.html')

def home_admin(request):
    return render(request, 'funcionarios/plantilla.html')

def solicitudes(request):
    solicitudes = solicitud.objects.all()
    print(solicitudes)
    return render(request, 'funcionarios/solicitudesAdmin/solicitudes.html', {'solicitudesAdmin':solicitudes})

def contacto(request):
    return render(request, 'paginas/contacto.html')


def usuarios(request):
    usuarios = cliente.objects.all()
    print(usuarios)
    return render(request, 'funcionarios/usuarios/clientesLista.html', {'usuarios':usuarios})  


def crear(request):
    formulario = clienteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('usuarios')
    return render(request, 'funcionarios/usuarios/crearCliente.html', { 'formulario':formulario} )


def productos(request):
    productos= producto.objects.all()
    print(productos)
    return render(request, 'funcionarios/productos/indexProd.html', {'productos':productos})


def editar(request, id):
    clienteEditado = cliente.objects.get(id=id)
    formulario = clienteForm(request.POST or None, request.FILES or None, instance=clienteEditado)
    
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('usuarios')
    
    return render(request, 'funcionarios/usuarios/editar.html', { 'formulario':formulario} )


def borrar(request, id):
    clienteBorrado = cliente.objects.get(id=id)
    clienteBorrado.delete()
    return redirect('usuarios')


def crearProd (request):
    prodForm = productoForm(request.POST or None, request.FILES or None)
    if prodForm.is_valid():
        prodForm.save()
        return redirect('productos')
    return render(request, 'funcionarios/productos/crearProd.html', { 'formProd':prodForm})

def editarProd(request, idProd):     
        productoEditado = producto.objects.get(idProd=idProd)
        prodForm = productoForm(request.POST or None, request.FILES or None, instance=productoEditado)       
        if prodForm.is_valid() and request.POST:
            prodForm.save()
            return redirect('productos')
        return render(request, 'funcionarios/productos/editarProd.html',{ 'formProd':prodForm})

def borrarProd(request, idProd):
    prodBorrado = producto.objects.get(idProd=idProd)
    prodBorrado.delete()
    return redirect('productos')

def salir(request):
    logout(request) 
    return redirect('login')

def clientes(request):
    return render (request,'clientes/plantClient.html')

def prodClient(request):
    productos= producto.objects.all()
    print(productos)
    return render(request, 'clientes/prodClient/indexProdClient.html', {'productos':productos})

def crearSold (request):
    soldForm = solicitudForm(request.POST or None, request.FILES or None)
    if soldForm.is_valid():
        soldForm.save()
        return redirect('solicitudes')
    return render(request, 'funcionarios/solicitudesAdmin/agregar.html', {'formSold':soldForm})

def editarSold(request):     
        return render(request, 'funcionarios/solicitudesAdmin/editarSold.html')

def borrarSold(request, idSold):
    soldBorrado = solicitud.objects.get(idSold=idSold)
    soldBorrado.delete()
    return redirect('solicitudes')
