from django.shortcuts import render , redirect
from .models import Factura, DetalleFactura
from Aplicaciones.Reserva.models import Reservacion
from Aplicaciones.Servicios.models import *
from autenticacion.decorators import admin_only, cache_not
from django.contrib import messages
from django.db import transaction
from datetime import date
from django.shortcuts import redirect, get_object_or_404
from decimal import Decimal

@cache_not
@admin_only
def facturaVista(request):
    factura_lista = Factura.objects.all()
    return render(request, 'AdminFactura/facturacion.html',{'factura_lista':factura_lista})

@cache_not
@admin_only
def eliminarFactura(id_factura):
    Facturas=Factura.objects.get(id_factura=id_factura)
    Facturas.delete()
    return redirect('facturaVista')

@cache_not
@admin_only
def edicionFactura(request,id_factura):
    facturaE=Factura.objects.get(id_factura=id_factura)
    return render (request,"AdminFactura/edicionfactura.html",{"factura":facturaE})

@cache_not
@admin_only
def editarFactura(request,id_factura):
    if request.method =='POST':
        estado=request.POST['txtEstado']
        
        Facturas=Factura.objects.get(id_factura=id_factura)
        Facturas.estado=estado
        Facturas.save()

        messages.success(request,'Factura Actualizada :D')

        return redirect('facturaVista')
    
#---------------Detalle de Factura ---------------------

@cache_not
@admin_only
def detallefacturaVista(request):
    Dfactura_lista = DetalleFactura.objects.all()
    return render(request, 'AdminFactura/detalleFactura.html',{'dfactura':Dfactura_lista})

@cache_not
@admin_only
def adicionDfactura(request):
    productos_restaurante = Restaurante.objects.all()
    productos_bar = Bar.objects.all()
    servicios_zonas_humedas = ZonasHumedas.objects.all()
    
    context = {
        'productos_restaurante': productos_restaurante,
        'productos_bar': productos_bar,
        'servicios_zonas_humedas': servicios_zonas_humedas,
    }

    return render(request,'AdminFactura/adicionDfactura.html',context)

@cache_not
@admin_only
def registrarDfactura(request):
    reserva = int(request.POST['id_reserva'])
    
    id_reservaF = Reservacion.objects.get(id_reserva=reserva)
    
    hoy = date.today()
    
    if id_reservaF and id_reservaF.fechasalida >= hoy:
        factura = get_object_or_404(Factura, reserva=reserva)
        producto_restaurante = request.POST.get('producto_restaurante', None)
        producto_bar = request.POST.get('producto_bar', None)
        servicio_zonas_humedas = request.POST.get('servicio_zonas_humedas', None)
        cantidad = int(request.POST['cantidad'])
        precio = 0
        
        restaurante_obj = Restaurante.objects.filter(Nombre=producto_restaurante).first() if producto_restaurante else None
        bar_obj = Bar.objects.filter(Nombre=producto_bar).first() if producto_bar else None
        zonas_humedas_obj = ZonasHumedas.objects.filter(Nombre=servicio_zonas_humedas).first() if servicio_zonas_humedas else None
        
        if restaurante_obj:
            precio = restaurante_obj.Precio
        if bar_obj:
            precio = bar_obj.Precio
        if zonas_humedas_obj:
            precio = zonas_humedas_obj.Precio
            
        subtotal = Decimal(str(precio)) * cantidad
        
        Dfactura = DetalleFactura.objects.create(
            id_factura=factura,
            producto_restaurante=restaurante_obj,
            producto_bar=bar_obj,
            servicio_zonas_humedas=zonas_humedas_obj,
            cantidad=cantidad,
            precio=precio,
            subtotal=subtotal
        )
        
        factura.total+=subtotal
        factura.save()
        
        return redirect('DfacturaVista')
    else:
        return redirect('adicionDfactura')

@cache_not    
@admin_only
def eliminarDFactura(id_detallefactura):
    DFactura=DetalleFactura.objects.get(id_detallefactura=id_detallefactura)
    DFactura.delete()
    return redirect('DfacturaVista')

#-----------Procesar pago PDF GENERADOR -------------------------
@cache_not
def ImprimirFactura(request , id_reserva):
    return render(request, 'AdminReserva/ImprimirFactura.html',{'id_reserva': id_reserva})

@cache_not
def ImprimiendoFactura(request, id_reserva):
    reserva = Reservacion.objects.get(id_reserva=id_reserva)
    factura = Factura.objects.get(reserva=reserva)
    context = {'factura': factura,'reserva':reserva}
    return render(request,'AdminReserva/ImprimirXD.html', context)

@cache_not
def procesarPago(request,id_reserva):
    reserva = Reservacion.objects.get(id_reserva=id_reserva)
    estado = "Pagado"
    total = reserva.precio

    factura = Factura.objects.create(
        reserva=reserva,
        estado=estado,
        total=total
    )
    
    reserva.estado = Reservacion.Confirmada
    reserva.save()
    
    return redirect('ImprimirFactura',id_reserva=id_reserva)


@transaction.atomic
def cerrar_estadia(id_reserva):
    factura_servicios = Factura.objects.filter(reserva_id=id_reserva, estado='Pendiente').first()
    
    if factura_servicios:
        total_servicios = sum(detalle.subtotal for detalle in factura_servicios.detalles.all())
        factura_servicios.total = total_servicios
        factura_servicios.estado = 'Pagado'
        factura_servicios.save()