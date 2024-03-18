from django.db import models

class Servicios (models.Model):
    Id_servicio=models.AutoField(primary_key=True, null=False, default=None)
    servicio=models.CharField(max_length=30, null=False, default=None)

class Restaurante(models.Model):
    Id_producto=models.BigAutoField(primary_key=True)
    TipoPlatillo=models.CharField(max_length=20)
    Nombre=models.CharField(max_length=50)
    Precio=models.FloatField()
    Id_servicio=models.ForeignKey(Servicios, on_delete=models.CASCADE, default=1)
    
    Uso = "En uso"
    NoUso = "No se usa"
    SinStock = "No hay Stock"
    
    estado_choices = [
        (Uso,'En uso'),
        (NoUso,'No se usa'),
        (SinStock,'No hay Stock')
    ]
    
    Estado = models.CharField(max_length = 25, choices=estado_choices, default='En uso') 

    db_table='restaurante'

    def __str__(self):
        texto="{0} ({1})"
        return texto.format(self.Nombre,self.Precio)
    
class Bar(models.Model):
    Id_producto=models.BigAutoField(primary_key=True) 
    TipoBebida=models.CharField(max_length=20)
    Nombre=models.CharField(max_length=50)
    Precio=models.FloatField()
    Id_servicio=models.ForeignKey(Servicios, on_delete=models.CASCADE, default=2)
    
    Uso = "En uso"
    NoUso = "No se usa"
    SinStock = "No hay Stock"
    
    estado_choices = [
        (Uso,'En uso'),
        (NoUso,'No se usa'),
        (SinStock,'No hay Stock') 
    ]
    
    Estado = models.CharField(max_length = 25, choices=estado_choices, default='En uso')

    db_table='bar'

    def __str__(self):
        texto="{0} ({1})"
        return texto.format(self.Nombre,self.Precio)
    
class ZonasHumedas(models.Model):
    Id_productoZH=models.BigAutoField(primary_key=True) 
    Nombre=models.CharField(max_length=40)
    Precio=models.FloatField()
    Id_servicio=models.ForeignKey(Servicios, on_delete=models.CASCADE, default=3)
    
    Uso = "En uso"
    NoUso = "No se usa"
    SinStock = "No hay Stock"
    
    estado_choices = [
        (Uso,'En uso'),
        (NoUso,'No se usa'),
        (SinStock,'No hay Stock')
    ]
    
    Estado = models.CharField(max_length = 25, choices=estado_choices, default='En uso')

    db_table='zonas_humedas'

    def __str__(self):
        texto="{0} ({1})"
        return texto.format(self.Nombre,self.Precio)


