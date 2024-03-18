from django import forms
from .models import Reservacion

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reservacion
        fields = ['usuario', 'habitacion','fecha_entrada', 'fecha_salida', 'cantidad_clientes', 'estado']
        widgets = {
            'fecha_entrada': forms.DateInput(attrs={'type': 'date'}),
            'fecha_salida': forms.DateInput(attrs={'type': 'date'}),
            'habitacion': forms.HiddenInput()
        }