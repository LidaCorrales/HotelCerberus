from django.shortcuts import render 
from autenticacion.decorators import untenticado_user, cache_not
from django.views.generic.base import TemplateView

@cache_not
@untenticado_user
def index(request):
    return render(request,"index.html")


class Error404view(TemplateView):
    template_name = "error_404.html"