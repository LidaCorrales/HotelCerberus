from django.db import models
from Aplicaciones.Habitaciones.models import Habitaciones
from autenticacion.models import CustomUser

class Reservacion(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Id_habitacion = models.ForeignKey(Habitaciones, on_delete=models.CASCADE)
    fechaentrada = models.DateField()
    fechasalida = models.DateField()
    cantidad_clientes = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    Por_confirmar = 'Por Confirmar'
    Confirmada = 'Confirmada'
    Cancelada = 'Cancelada'
    Estado_Choices_R = [
        (Por_confirmar, 'Por Confirmar'),
        (Confirmada,' Confirmada'),
        (Cancelada, 'Cancelada')
    ]
    
    estado = models.CharField(max_length=25, choices=Estado_Choices_R, default=Por_confirmar)