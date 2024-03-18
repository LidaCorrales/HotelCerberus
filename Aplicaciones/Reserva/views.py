from django.shortcuts import render, redirect
from .models import Reservacion
from django.contrib import messages
from autenticacion.decorators import admin_only, autorizacion_login_user, cache_not, empleados_only
from Aplicaciones.Habitaciones.models import Habitaciones, tipoHabitaciones
from .models import CustomUser
from datetime import datetime
from django.shortcuts import get_object_or_404

@cache_not
@empleados_only
def ReservasAdmin(request):
    lista_reserva= Reservacion.objects.all()
    messages.success(request,'Reservas Listadas :D')
    return render(request, 'AdminReserva/reservas.html',{'lista_reserva':lista_reserva})

@cache_not
@autorizacion_login_user
def reservaClienteView(request, Id_habitacion):
    tipos = tipoHabitaciones.objects.all()
    context = {'tipo_habitacion': tipos, 'Id_habitacion': Id_habitacion}
    return render(request, 'usuario/reserva.html', context)

@cache_not
@autorizacion_login_user
def MisReservas(request):
    resv = Reservacion.objects.all()
    return render(request, 'usuario/ReservasUsuario.html', {'resv':resv})


@cache_not
def ReservaUsuario(request):
    return render(request, 'usuario/reserva.html')

@cache_not
def ReservaHecha(request):
    return render(request, 'usuario/reservaExitosa.html')

@autorizacion_login_user
def registroReserva(request, Id_habitacion):
    error_message = ''
    
    if request.method == 'POST':
        usuario = request.user  

        habitacion = get_object_or_404(Habitaciones, Id_habitacion=Id_habitacion)
        tipo_habitacion = habitacion.id_tipo_hab
        habitacion_disponible = get_object_or_404(Habitaciones, Id_habitacion=Id_habitacion, estado=Habitaciones.Disponible)

        fecha_entrada_str = request.POST.get('fechaentrada')
        fecha_salida_str = request.POST.get('fechasalida')
        cantidad_clientes = int(request.POST.get('cantidad_clientes'))
        
        if cantidad_clientes > tipo_habitacion.espacio:
            error_message = 'No hay habitaciones con este cantidad de personas'

        if error_message:
            return render(request, 'usuario/reserva.html', {'error_message': error_message, 'Id_habitacion': Id_habitacion})
        else:
            fecha_entrada = datetime.strptime(fecha_entrada_str, '%Y-%m-%d').date()
            fecha_salida = datetime.strptime(fecha_salida_str, '%Y-%m-%d').date()
            
            dias_reserva = (fecha_salida - fecha_entrada).days
            precio_total = dias_reserva * habitacion_disponible.id_tipo_hab.precio
        
        reserva = Reservacion.objects.create(
            username=usuario,
            Id_habitacion=habitacion_disponible,
            fechaentrada=fecha_entrada,
            fechasalida=fecha_salida,
            cantidad_clientes=cantidad_clientes,
            precio=precio_total,
            estado=Reservacion.Por_confirmar
        )
        
        habitacion_disponible.estado = Habitaciones.Ocupada
        habitacion_disponible.save()
        
        
        return redirect('ReservaRegistrada')
    else:
        return render(request, 'usuario/reserva.html', {'Id_habitacion': Id_habitacion})

#-----------ADMIN------------------

@cache_not
@empleados_only
def registraReservaAdmin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user = CustomUser.objects.get(username=username)
        Id_habitacion_str = request.POST.get('Id_habitacion')        
        Id_habitacion = Habitaciones.objects.get(Id_habitacion=Id_habitacion_str) 
        fechaentrada_str = request.POST.get('fechaentrada') 
        fechasalida_str = request.POST.get('fechasalida')
        cantidad_clientes = int(request.POST.get('cantidad_clientes'))

        tipo_habitacion = Id_habitacion.id_tipo_hab
        error_message = None

        if cantidad_clientes > tipo_habitacion.espacio:
            error_message = 'No hay habitaciones con este cantidad de personas'

        if error_message:
            return render(request, 'AdminReserva/reservas.html', {'error_message': error_message, 'Id_habitacion': Id_habitacion})
        else:
            fechaentrada = datetime.strptime(fechaentrada_str, '%Y-%m-%d').date()
            fechasalida = datetime.strptime(fechasalida_str, '%Y-%m-%d').date()
            
            dias_reserva = (fechasalida - fechaentrada).days
            precio_total = dias_reserva * Id_habitacion.id_tipo_hab.precio

        reserva = Reservacion.objects.create(
            username=user,
            Id_habitacion=Id_habitacion,
            fechaentrada=fechaentrada,
            fechasalida=fechasalida,
            cantidad_clientes=cantidad_clientes,
            precio=precio_total,
            estado=Reservacion.Por_confirmar
        )
        
        habitacion = Id_habitacion
        habitacion.estado = Habitaciones.Ocupada
        habitacion.save()

        return redirect('reservas')
    else:
        return render(request, 'AdminReserva/reservas.html')

@cache_not
@empleados_only
def editarReservaAdmin(request, id_reserva):
    reserva_lista= Reservacion.objects.get(id_reserva=id_reserva)
    return render(request, 'AdminReserva/edicionReserva.html',{'reserva_lista':reserva_lista})

@cache_not
@empleados_only
def editarReserva(request, id_reserva):
    reserva=get_object_or_404(Reservacion, pk=id_reserva)
    if request.method == 'POST':
        fechaentrada=request.POST['txtEntrada']
        fechasalida=request.POST['txtSalida']
        cantidad_clientes=request.POST['txtCantidad']
        estado=request.POST['txtEstado']

        reserva.fechaentrada = fechaentrada
        reserva.fechasalida = fechasalida
        reserva.cantidad_clientes = cantidad_clientes
        reserva.estado = estado
        reserva.save()

        messages.success(request,'Reserva Actualizadas :D')

        return redirect('reservas')
    
@admin_only    
def eliminarReserva(request, id_reserva):
    reservas = Reservacion.objects.get(id_reserva=id_reserva)
    reservas.delete()
    messages.success(request,'Habitaciones Eliminadas D:')
    return redirect('/reservas/')

#------------Confirmas datos de pago------------------
@cache_not
def confirmarReservaPago(request):
    id_reserva = request.GET.get('id_reserva')
    reserva = get_object_or_404(Reservacion, id_reserva=id_reserva) 
    
    if request.method == 'POST':
        pass
    
    fechaentrada = reserva.fechaentrada.strftime('%Y-%m-%d')
    fechasalida = reserva.fechasalida.strftime('%Y-%m-%d')
        
    context = {
            'id_reserva': id_reserva,
            'username': request.user,
            'Id_habitacion': reserva.Id_habitacion.Id_habitacion,
            'fechaentrada': fechaentrada,
            'fechasalida': fechasalida,   
            'cantidad_clientes': reserva.cantidad_clientes,
            'precio': reserva.precio,
        }
    return render(request, 'AdminReserva/pagoReserva.html', context)

@cache_not
def VerReservaPago(request):
    id_reserva = request.GET.get('id_reserva')
    reserva = get_object_or_404(Reservacion, id_reserva=id_reserva) 
    
    if request.method == 'POST':
        pass
    
    fechaentrada = reserva.fechaentrada.strftime('%Y-%m-%d')
    fechasalida = reserva.fechasalida.strftime('%Y-%m-%d')
        
    context = {
            'id_reserva': id_reserva,
            'username': request.user,
            'Id_habitacion': reserva.Id_habitacion.Id_habitacion,
            'fechaentrada': fechaentrada,
            'fechasalida': fechasalida,   
            'cantidad_clientes': reserva.cantidad_clientes,
            'precio': reserva.precio,
        }
    return render(request, 'AdminReserva/verReserva.html', context)

