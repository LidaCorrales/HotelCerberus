from django.urls import path
from . import views

urlpatterns = [
    path('Factura/', views.facturaVista, name='facturaVista'), 
    path('Factura/edicionFactura/<id_factura>', views.edicionFactura),
    path('Factura/editarFactura/<id_factura>', views.editarFactura,name='editarFactura'),
    path('Factura/eliminarFactura/<id_factura>',views.eliminarFactura),
    path('FacturaPago/<id_reserva>',views.procesarPago, name='procesarPago'),
    path('ImprimirFactura/<id_reserva>',views.ImprimirFactura, name='ImprimirFactura'),
    path('ImprimiendoFactura/<id_reserva>',views.ImprimiendoFactura, name='ImprimiendoFactura'),
    path('FacturasCliente/<id_reserva>',views.pageusuFacturas, name='ViewFacturas'),
    #Detalle Factura ------------
    path('Dfactura/',views.detallefacturaVista, name='DfacturaVista'),
    path('Dfactura/adicionarDfactura',views.adicionDfactura,name='adicionDfactura'),
    path('Dfactura/registrarDfactura',views.registrarDfactura,name='registrarDfactura'),

    path('DetallesPago/',views.procesarPagoDetalle, name='procesarPagoD'),
    path('ImprimirFacturaServicios/<id_reserva>',views.ImprimirServicios, name='ImprimirFacturaS'),
    path('ImprimiendoFacturaServicios/<id_reserva>',views.ImprimiendoFacturaServicios, name='ImprimiendoFacturaS'),
    #path('Dfactura/edicionDfactura/<id_detallefactura>',views.edicionDFactura),
    #path('Dfactura/editarDfactura/<id_detallefactura>',views.editarDFactura,name='editarDfactura'),
    path('Dfactura/eliminarDfactura/<id_detallefactura>',views.eliminarDFactura),
]