from django.shortcuts import render, redirect
from . models import Habitaciones, tipoHabitaciones
from django.contrib import messages

from autenticacion.decorators import admin_only, cache_not


#Vistas de habitacion
@cache_not
@admin_only
def home(request):
    habitacion=Habitaciones.objects.all()
    messages.success(request,'Habitaciones Listados :D')
    tipohab = tipoHabitaciones.objects.all()
    return render(request,"AdminHabitacion/habitaciones.html",{"habitacion":habitacion, "tipohab": tipohab})

@cache_not
def habitaciones(request):
    habitaciones = Habitaciones.objects.all()
    return render(request, "usuario/habitacion.html", {'habitaciones': habitaciones})

@cache_not
def vista_habitacion_sencilla(request):
    habitaciones = Habitaciones.objects.all()
    return render(request, "habitacionesUsuario/Sencilla.html", {'habitaciones': habitaciones})

@cache_not
def vista_habitacion_doble(request):
    habitaciones = Habitaciones.objects.all()
    return render(request, "habitacionesUsuario/Doble.html", {'habitaciones': habitaciones})

@cache_not
def vista_habitacion_triple(request):
    habitaciones = Habitaciones.objects.all()
    return render(request, "habitacionesUsuario/Triple.html", {'habitaciones': habitaciones})

@cache_not
def vista_habitacion_suit(request):
    habitaciones = Habitaciones.objects.all()
    return render(request, "habitacionesUsuario/Suites.html", {'habitaciones': habitaciones})

@cache_not
def vista_only_hab(request, Id_habitacion):
    hab = Habitaciones.objects.get(Id_habitacion=Id_habitacion)
    return render(request, 'habitacionesUsuario/vistaOnlyHab.html', {'habitacion': hab})

#Funciones
@cache_not
@admin_only
def registroHab(request):
    if request.method == 'POST':
        id_tipo_hab_id = int(request.POST.get('txtTipo'))
        estado = request.POST.get('txtEstado')

        tipo_habitacion = tipoHabitaciones.objects.get(pk=id_tipo_hab_id)

        habitacion = Habitaciones.objects.create(
            id_tipo_hab=tipo_habitacion, estado=estado
        )
    messages.success(request,'Habitacion añadida :D')
    return redirect('/Habitaciones/')

@cache_not
@admin_only
def edicionHab(request, Id_habitacion):
    habitacion = Habitaciones.objects.get(Id_habitacion=Id_habitacion)
    tipohab = tipoHabitaciones.objects.all()
    return render(request, "AdminHabitacion/edicionHab.html", {"habitacion":habitacion, "tipohab": tipohab})

@cache_not
@admin_only
def editarHab(request):
    if request.method == 'POST':
        Id_habitacion=request.POST['txtIdHab']
        id_tipo_hab=request.POST['txtTipo']
        estado=request.POST['txtEstado']
        
        tipo_habitacion = tipoHabitaciones.objects.get(pk=id_tipo_hab)

        habitacion = Habitaciones.objects.get(Id_habitacion=Id_habitacion)
        habitacion.Id_habitacion = Id_habitacion
        habitacion.id_tipo_hab = tipo_habitacion
        habitacion.estado = estado
        habitacion.save()
    
        messages.success(request,'Habitaciones Actualizadas :D')
        
        return redirect("registroHab")

@cache_not
@admin_only
def eliminacionHab(request, Id_habitacion):
    habitacion = Habitaciones.objects.get(Id_habitacion=Id_habitacion)
    habitacion.delete()

    messages.success(request,'Habitaciones Eliminadas D:')

    return redirect('/Habitaciones/')
