from django.contrib import messages
from django.shortcuts import render, redirect


def login_entrada(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        if email.lower().endswith('@utpl.edu.ec'):

            return redirect('index')
        else:
            messages.error(request, 'El correo debe pertenecer al dominio @utpl.edu.ec')
            return render(request, 'core/login_entrada.html')

    return render(request, 'core/login_entrada.html')


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
