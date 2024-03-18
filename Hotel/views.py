from django.shortcuts import render
from autenticacion.decorators import untenticado_user, cache_not

@cache_not
@untenticado_user
def index(request):
    return render(request,"index.html")