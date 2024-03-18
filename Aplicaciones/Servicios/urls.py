from django.urls import path
from . import views

urlpatterns=[
    path('IndexRes',views.homeRest, name="IndexRes"),
    path('registroRestaurante/',views.registroRestaurante, name='registroRestaurante'),
    path('edicionRestaurante/<Id_producto>',views.edicionRestaurante),
    path('editarRestaurante/',views.editarRestaurante, name='editarRestaurante'),
    path('eliminacionRestaurante/<Id_producto>',views.eliminacionRestaurante),
    #---------paths de bar--------------------
    path('IndexBar/',views.homeBar, name="IndexBar"),
    path('IndexBar/registroBar/',views.registroBar, name='registroBar'),
    path('IndexBar/edicionBar/<Id_producto>',views.edicionBar),
    path('IndexBar/editarBar/',views.editarBar, name='editarBar'),
    path('IndexBar/eliminacionBar/<Id_producto>',views.eliminacionBar),
    #---------paths de zonas humedas---------------
    path('IndexZH/',views.homeZH, name="IndexZH"),
    path('IndexZH/registroZH/',views.registroZH, name='registroZH'),
    path('IndexZH/edicionZH/<Id_productoZH>',views.edicionZH),
    path('IndexZH/editarZH/',views.editarZH, name='editarZH'),
    path('IndexZH/eliminacionZH/<Id_productoZH>',views.eliminacionZH)
]