from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import SolicitudSocioForm


def hazte_socio(request):
    if request.method == 'POST':
        # Se crea una instancia del formulario con los datos POST y los archivos
        form = SolicitudSocioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Se añade un mensaje de éxito para mostrarlo al usuario
            messages.success(request,
                             '¡Tu solicitud ha sido enviada con éxito! Nos pondremos en contacto contigo pronto.')
            # Redirige a la página principal
            return redirect('core:index')
    else:
        # Si es una petición GET, se crea un formulario vacío
        form = SolicitudSocioForm()

    context = {'form': form}
    return render(request, "socio/hazte_socio.html", context)
