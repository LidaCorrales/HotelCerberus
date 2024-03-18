from django.http import HttpResponse
from django.shortcuts import redirect
from functools import wraps

def cache_not(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        response = view_func(request,*args, **kwargs)
        if isinstance(response, HttpResponse):
            response['Cache-Control'] = 'no-store, no-cache, must-revalidate'
            response['Pragma'] = 'no-cache'
            response['Expires'] = '0'
            return response
        else:
            return redirect('index')

    return _wrapped_view

def untenticado_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.is_authenticated:
            group = request.user.groups.all()[0].name
            if group == 'cliente':
                return redirect('paginausu')
            elif group == 'admin':
                return redirect('paginadmin')
            elif group == 'recepcionista':
                return redirect('paginarecepcionista')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def autorizados_user(autorizados_user=[]):
    def decorator (view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in autorizados_user:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('No esta autorizado :/')
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'cliente':
            return redirect('paginausu')
        elif group == 'admin':
            return view_func(request,*args,**kwargs)
        elif group == 'empleado':
            return redirect('paginarecepcionista')

    return wrapper_function

def autorizacion_login_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')
        
    return wrapper_func

def empleados_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'cliente':
            return redirect('paginausu')
        elif group == 'admin':
            return view_func(request,*args,**kwargs)
        elif group == 'recepcionista':
            return view_func(request,*args,**kwargs)

    return wrapper_function