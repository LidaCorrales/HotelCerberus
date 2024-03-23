from django.shortcuts import render
from autenticacion.decorators import untenticado_user, cache_not
from autenticacion.models import ArchivoPDF

@cache_not
@untenticado_user
def index(request):
    pdf_usuario = ArchivoPDF.objects.filter(title="Manual_de_Usuarios_HotelCerberus").first()
    return render(request,"index.html", {'pdf_usuario': pdf_usuario})