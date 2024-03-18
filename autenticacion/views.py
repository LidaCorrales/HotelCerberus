from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout

from .decorators import admin_only, autorizados_user, autorizacion_login_user

from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, ActualizacionForm
from .decorators import untenticado_user, cache_not
from django.contrib.auth.models import Group

from .forms import CustomUserCreationForm
from .models import tipoDocumento, CustomUser
from Aplicaciones.Habitaciones.models import Habitaciones, tipoHabitaciones

@cache_not
@admin_only
def homeUsu(request):
    usuarios=CustomUser.objects.all()
    messages.success(request,'Usuario Listados :D')
    return render(request,"AdminUsuario/usuario.html",{"usuarios":usuarios})

@cache_not
@admin_only
def registroUsu(request):
    form = CustomUserCreationForm()
    tipos_documento = tipoDocumento.objects.all()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='cliente')
            user.groups.add(group)
            return redirect('UsuarioIndex')
    else:
        form = CustomUserCreationForm() 

    context = {'form': form, 'tipos_documento': tipos_documento}
    return render(request, "AdminUsuario/usuario.html", context)

@cache_not
@admin_only
def editarUsu(request, id):
    user = CustomUser.objects.get(id=id)
    Usuarios = CustomUser.objects.all()
    form= ActualizacionForm(instance=user)

    if request.method=="POST":
        form=ActualizacionForm(request.POST, instance=user)
        if form.is_valid():
            user=form.save()
            return redirect('UsuarioIndex')
        
    context = {'form':form, 'usuarios':Usuarios} 
    return render(request,"AdminUsuario/edicionUsu.html", context)

@cache_not
@admin_only
def eliminacionUsu(request, id):
    usuarios = CustomUser.objects.get(id=id)
    if request.method=="POST":
        usuarios.delete()
        messages.success(request,'Usuario Eliminado D:')
        return redirect('UsuarioIndex')
    context = {'user':usuarios}
    return render(request,"AdminUsuario/eliminacionUsu.html", context)

##########################################################
@cache_not
@untenticado_user
def PaginaRegistrar(request):
    form = CustomUserCreationForm()
    tipos_documento = tipoDocumento.objects.all()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='cliente')
            user.groups.add(group)
            messages.success(request, f'Cuenta creada para {username}')
            return redirect('login')

    context = {'form': form, 'tipos_documento': tipos_documento}
    return render(request, "registro/registro.html", context)

@cache_not
@untenticado_user
def PaginaLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        group = None

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            group = request.user.groups.all()[0].name
            if group == 'cliente':
                return redirect('paginausu')
            elif group == 'admin':
                return redirect('paginadmin')
            elif group == 'recepcionista':
                return redirect('paginarecepcionista')
        else:
            messages.info(request, 'Usuario o Contraseña incorrectos...')

    context = {}
    return render (request, 'registro/login.html', context)

@cache_not
def logoutUser(request):
    logout(request)
    return redirect('index')

@cache_not   
@autorizados_user(autorizados_user=['admin'])    
def pageadmin(request):
        return render(request,'administrador/admin.html')
    
#Views de paginas del usuario
@cache_not
def userPage(request):
    context = {}
    return render(request,'autenticacion/usuario/user.html', context)

@cache_not
@autorizacion_login_user 
def pageusu(request):
        return render(request,'usuario/user.html')

@cache_not
@autorizacion_login_user
def pageusureserva(request):
    return render(request,'usuario/reserva.html')

@cache_not
def pageusuRes(request):
    return render(request, 'usuario/restaurante.html')

@cache_not
def pageusuBar(request):
    return render(request, 'usuario/bar.html')

@cache_not
def pageusuZH(request):
    return render(request, 'usuario/zonas_humedas.html')

@cache_not
@autorizacion_login_user
def pageusuHabitaciones(request):
    return render(request, 'usuario/habitacion.html')

#----------------------empleado-----------------
@cache_not
@autorizacion_login_user
def recepcionista(request):
    return render(request,'empleado/recepcionista.html')

@cache_not
@autorizacion_login_user
def HabitacionesE(request):
    habitacion=Habitaciones.objects.all()
    return render(request,'empleado/habitacionesE.html', {"habitacion":habitacion})
