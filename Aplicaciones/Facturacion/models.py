from django.db import models
from Aplicaciones.Reserva.models import Reservacion
from Aplicaciones.Servicios.models import  Bar, Restaurante, ZonasHumedas

class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    reserva = models.ForeignKey(Reservacion, on_delete=models.CASCADE)
    fecha_emitida = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=15)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class DetalleFactura(models.Model):
    id_detallefactura = models.AutoField(primary_key=True)
    id_factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    producto_restaurante = models.ForeignKey(Restaurante, null=True, blank=True, on_delete=models.SET_NULL)
    producto_bar = models.ForeignKey(Bar, null=True, blank=True, on_delete=models.SET_NULL)
    servicio_zonas_humedas = models.ForeignKey(ZonasHumedas, null=True, blank=True, on_delete=models.SET_NULL)
    cantidad = models.IntegerField(default=1)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def save(self, *args, **kwargs):
        self.subtotal = self.precio * self.cantidad
        super(DetalleFactura, self).save(*args, **kwargs)
        
    def actualizar_total_factura(self):
        total = sum(detalle.subtotal for detalle in DetalleFactura.objects.filter(factura=self.factura))
        self.factura.total = total
        self.factura.save()

    def delete(self, *args, **kwargs):
        super(DetalleFactura, self).delete(*args, **kwargs)
        self.actualizar_total_factura()