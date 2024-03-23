from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',views.PaginaRegistrar, name="register"),
    path('login/',views.PaginaLogin, name="login"),
    path('logout/',views.logoutUser, name='logout'),
    path('user/',views.userPage, name='userpage'),
    path('paginausu/',views.pageusu, name='paginausu'),
    path('paginadmin/',views.pageadmin, name='paginadmin'), 
    
    path('restaurante/',views.pageusuRes, name='RestauranteUsuario'),
    path('bar/',views.pageusuBar, name='BarUsuario'),
    path('zonashumedas/',views.pageusuZH, name='ZonasHumedasUsuario'),
    path('reserva/',views.pageusureserva, name='ReservaUsuario'),
    path('Habitaciones/',views.pageusuHabitaciones, name='HabitacionesUsuario'),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="registro/password_reset.html"), name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="registro/password_reset_send.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="registro/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="registro/password_reset_done.html"), name="password_reset_complete"),

    path('Usuarios/',views.homeUsu, name="UsuarioIndex"),
    path('Usuarios/registroUsu/',views.registroUsu, name='registroUsuario'),
    path('Usuarios/editarUsu/<id>',views.editarUsu, name='editarUsuario'),
    path('Usuarios/eliminacionUsu/<id>',views.eliminacionUsu),

    #------------empleado-------------
    path('Empleados/',views.recepcionista, name='paginarecepcionista'),
    path('EmpleadosHab/',views.HabitacionesE, name='habitacionesE'),
    path('EmpleadosS/',views.ServiciosEmpleado, name='PagoServiciosEmpleado'),

    #---------PDF admin ------------
    path('UploadPDF/', views.upload_pdf, name='subiendoPDF'),
    path('descargarPDF/<int:pk>/',views.descargarPDF,name='descargarPDF')
]
