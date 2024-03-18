from django.urls import path, include
from . import views


urlpatterns=[
    path('Reservas',views.ReservasAdmin, name="reservas"),
    path('ReservaUsuario',views.registroReserva, name="ReservaUsuario"),
    path('EditarReserva/<int:id_reserva>/',views.editarReserva, name="ediReserva"),

    path('autenticacion/',include('autenticacion.urls')),
    
    #Views Cliente
    path('ReservaCliente<int:Id_habitacion>/',views.reservaClienteView,name='ReservaCliente'),
    path('RegistroReserva/<int:Id_habitacion>/',views.registroReserva, name="RegistroReserva"),
    path('ReservaRegistrada',views.ReservaHecha, name="ReservaRegistrada"),
    path('ReservasUsuaario',views.MisReservas, name="MisReservas"),
    path('confirmarReservaPago/',views.confirmarReservaPago,name='confirmarReservaPago'),
    path('verReservaPago/',views.VerReservaPago,name='verReservaPago'),
    #Views Admin
    path('registrarReservaAdmin/', views.registraReservaAdmin, name='registraReservaAdmin'),
    path('editarReservaAdmin/<int:id_reserva>/', views.editarReservaAdmin, name='editarReservaAdmin'),
]