from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name="Habitacion"),
    path('registroHab/',views.registroHab, name="registroHab"),
    path('edicionHab/<Id_habitacion>',views.edicionHab),
    path('editarHab/',views.editarHab, name="editarHab"),
    path('eliminacionHab/<Id_habitacion>',views.eliminacionHab),
    path('Habitaciones/habitacion/', views.habitaciones, name='Habitaciones'),
    
    path('HabSencilla/',views.vista_habitacion_sencilla, name='HabitacionSencilla'),
    path('HabDoble/',views.vista_habitacion_doble, name='HabitacionDoble'),
    path('HabTriple/',views.vista_habitacion_triple, name='HabitacionTriple'),
    path('HabSuites/',views.vista_habitacion_suit, name='HabitacionSuites'),
    path('VistaHabitacion<int:Id_habitacion>/',views.vista_only_hab,name='VistaHabitacion'),
]