from django.shortcuts import render, redirect
from . models import Restaurante, Bar, ZonasHumedas
from django.contrib import messages

from autenticacion.decorators import admin_only, cache_not

@cache_not
@admin_only
def homeRest(request):
    restaurante=Restaurante.objects.all()
    messages.success(request,'Restaurantes Listados :D')
    return render(request,"Servicios/Restaurante/restaurante.html",{"restaurante":restaurante})

@cache_not
@admin_only
def registroRestaurante(request):
    Id_producto=request.POST['txtId']
    TipoPlatillo=request.POST['txtPlatillo']
    Nombre=request.POST['txtNombrePlato']
    Precio=request.POST['txtPrecio']

    restaurante = Restaurante.objects.create(
        Id_producto=Id_producto, TipoPlatillo=TipoPlatillo, Nombre=Nombre, Precio=Precio)
    messages.success(request,'Producto añadido :D')
    return redirect('/Servicios/IndexRes')

@cache_not
@admin_only
def edicionRestaurante(request, Id_producto):
    restaurante = Restaurante.objects.get(Id_producto=Id_producto)
    return render(request, "Servicios/Restaurante/edicionRes.html", {"restaurante":restaurante})

@cache_not
@admin_only
def editarRestaurante(request):
    if request.method == 'POST':
        Id_producto=request.POST['txtId']
        TipoPlatillo=request.POST['txtPlatillo']
        Nombre=request.POST['txtNombrePlato']
        Precio=request.POST['txtPrecio']
        Estado=request.POST['txtEstado']

        restaurante = Restaurante.objects.get(Id_producto=Id_producto)
        restaurante.Id_producto = Id_producto
        restaurante.TipoPlatillo = TipoPlatillo
        restaurante.Nombre = Nombre
        restaurante.Precio = Precio
        restaurante.Estado = Estado
        restaurante.save()

        messages.success(request,'Producto Actualizado :D')

        return redirect('/Servicios/IndexRes')

@cache_not
@admin_only
def eliminacionRestaurante(request, Id_producto):
    restaurante = Restaurante.objects.get(Id_producto=Id_producto)
    restaurante.delete()

    messages.success(request,'Producto Eliminado D:')

    return redirect('/Servicios/IndexRes')


#---------------------Servicio BAR -------------------------------------
@cache_not
@admin_only
def homeBar(request):
    bar=Bar.objects.all()
    messages.success(request,'Bar Listados :D')
    return render(request,"Servicios/Bar/bar.html",{"bar":bar})

@cache_not
@admin_only
def registroBar(request):
    Id_producto=request.POST['txtIdBar']
    TipoBebida=request.POST['txtBebida']
    Nombre=request.POST['txtNombreBebida']
    Precio=request.POST['txtPrecio']

    bar = Bar.objects.create(
        Id_producto=Id_producto, TipoBebida=TipoBebida, Nombre=Nombre, Precio=Precio)
    messages.success(request,'Producto añadido :D')
    return redirect('/Servicios/IndexBar/')

@cache_not
@admin_only
def edicionBar(request, Id_producto):
    bar = Bar.objects.get(Id_producto=Id_producto)
    return render(request, "Servicios/Bar/edicionBar.html", {"bar":bar})

@cache_not
@admin_only
def editarBar(request):
    Id_producto=request.POST['txtIdBar']
    TipoBebida=request.POST['txtBebida']
    Nombre=request.POST['txtNombreBebida']
    Precio=request.POST['txtPrecio']
    Estado=request.POST['txtEstado']

    bar = Bar.objects.get(Id_producto=Id_producto)
    bar.Id_producto =Id_producto
    bar.TipoBebida = TipoBebida
    bar.Nombre = Nombre
    bar.Precio = Precio
    bar.Estado = Estado
    bar.save()

    messages.success(request,'Producto Actualizado :D')

    return redirect('/Servicios/IndexBar/')

@cache_not
@admin_only
def eliminacionBar(request, Id_producto):
    bar = Bar.objects.get(Id_producto=Id_producto)
    bar.delete()

    messages.success(request,'Producto Eliminado D:')

    return redirect('/Servicios/IndexBar/')

#---------------------Servicio Zonas Humedas----------------
@cache_not
@admin_only
def homeZH(request):
    zh=ZonasHumedas.objects.all()
    messages.success(request,'Zonas Humedas Listados :D')
    return render(request,"Servicios/ZH/zonashumedas.html",{"zh":zh})

@cache_not
@admin_only
def registroZH(request):
    Id_productoZH=request.POST['txtIdZH']
    Nombre=request.POST['txtNombreZH']
    Precio=request.POST['txtPrecio']

    zh = ZonasHumedas.objects.create(
        Id_productoZH=Id_productoZH, Nombre=Nombre, Precio=Precio)
    messages.success(request,'Producto añadido :D')

    return redirect('/Servicios/IndexZH/')

@cache_not
@admin_only
def edicionZH(request, Id_productoZH):
    zh = ZonasHumedas.objects.get(Id_productoZH=Id_productoZH)
    return render(request, "Servicios/ZH/edicionZH.html", {"zh":zh})

@cache_not
@admin_only
def editarZH(request):
    Id_productoZH=request.POST['txtIdZH']
    Nombre=request.POST['txtNombreZH']
    Precio=request.POST['txtPrecio']
    Estado=request.POST['txtEstado']

    zh = ZonasHumedas.objects.get(Id_productoZH=Id_productoZH)
    zh.Id_productoZH = Id_productoZH
    zh.Nombre = Nombre
    zh.Precio = Precio
    zh.Estado = Estado
    zh.save()

    messages.success(request,'Producto Actualizado :D')

    return redirect('/Servicios/IndexZH/')

@cache_not
@admin_only
def eliminacionZH(request, Id_productoZH):
    zh = ZonasHumedas.objects.get(Id_productoZH=Id_productoZH)
    zh.delete()

    messages.success(request,'Producto Eliminado D:')

    return redirect('/Servicios/IndexZH/')