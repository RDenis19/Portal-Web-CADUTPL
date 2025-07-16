from django.shortcuts import render

# Create your views here.
def hazte_socio(request):
    context = {}
    return render(request, "socio/hazte_socio.html", context)