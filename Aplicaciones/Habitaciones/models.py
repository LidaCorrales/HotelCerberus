from django.db import models

class tipoHabitaciones(models.Model):
    Sencilla = 'Sencilla'
    Doble = 'Doble'
    Triple ='Triple'
    Suite = 'Suite'
    TipoH_Choices =[
        (Sencilla, 'Sencilla'),
        (Doble, 'Doble'),
        (Triple, 'Triple'),
        (Suite, 'Suite')
    ]
    id_tipo_hab=models.AutoField(primary_key=True)
    tipo=models.CharField(max_length=30, choices=TipoH_Choices, default=Sencilla)
    descripcion=models.CharField(max_length=50)
    espacio=models.IntegerField()
    precio=models.FloatField()
    
class Habitaciones(models.Model):
    Disponible = 'Disponible'
    Ocupada = 'Ocupada'
    Mantenimiento ='Mantenimiento'
    Estado_Choices =[
        (Disponible, 'Disponible'),
        (Ocupada, 'Ocupada'),
        (Mantenimiento, 'Mantenimiento')
    ]
    Id_habitacion=models.BigAutoField(primary_key=True)
    estado=models.CharField(max_length=30, choices=Estado_Choices, default=Disponible)
    id_tipo_hab= models.ForeignKey(tipoHabitaciones, on_delete=models.CASCADE, default=None)

    db_table='habitación'

    def __str__(self):
        texto="{0} ({1})"
        return texto.format(self.id_tipo_hab)
