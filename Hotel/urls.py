"""
URL configuration for Hotel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
##
from django.conf.urls import handler404
#
from Hotel.views import Error404view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('autenticacion/',include('autenticacion.urls')),
    path('Servicios/',include('Aplicaciones.Servicios.urls')),
    path('Habitaciones/',include('Aplicaciones.Habitaciones.urls')),
    path('Reservas/',include('Aplicaciones.Reserva.urls')),
    path('Facturacion/',include('Aplicaciones.Facturacion.urls')),
    #
    path('<path:dummy>/', views.Error404view.as_view(), name='error_404'),  # Captura todas las URL que no coincidan con las anteriores
]

handler404 = Error404view.as_view()