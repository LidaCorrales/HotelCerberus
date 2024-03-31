from django.contrib.auth.models import AbstractUser
from django.db import models

class tipoDocumento(models.Model):
    idTipo = models.IntegerField(primary_key=True)
    documento = models.CharField(max_length=30)

class CustomUser(AbstractUser):
    idTipo = models.ForeignKey(tipoDocumento, on_delete=models.CASCADE, null=True, default=None)
    numdoc = models.IntegerField(null=True, default=None)
    telefono = models.BigIntegerField(null=True, default=None)
    
    Activo = 'Activo'
    Inactivo = 'Inactivo'
    
    estado_choices =[
        (Activo, 'Activo'),
        (Inactivo, 'Inactivo'), #Choices para estado
    ]
    
    is_active = models.CharField(max_length=30, choices=estado_choices, default=Activo) 
