from django.urls import path
from . import views

app_name = 'socio'

urlpatterns = [
    # URL para la página "Hazte Socio"
    # Se accederá a ella a través de /hazte-socio/
    path("hazte-socio/", views.hazte_socio, name="hazte_socio"),
]