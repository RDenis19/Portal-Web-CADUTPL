from django.shortcuts import render

def login(request):
    return render(request, 'core/login.html')

def index(request):
    return render(request, 'core/index.html')

def ahorros(request):
    return render(request, 'core/ahorros.html')

def creditos(request):
    return render(request, 'core/creditos.html')

def servicios(request):
    return render(request, 'core/servicios.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def noticias(request):
    return render(request, 'core/noticias.html')

def haste_socio(request):
    return render(request, 'core/haste_socio.html')

def login_ingreso(request):
    return render(request, 'core/login_ingreso.html')
