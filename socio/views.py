from django.shortcuts import render


def hazte_socio(request):
    context = {}
    return render(request, "socio/hazte_socio.html", context)
