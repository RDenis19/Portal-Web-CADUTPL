from django.urls import path

from . import views

app_name = 'socio'

urlpatterns = [
    path("hazte-socio/", views.hazte_socio, name="hazte_socio"),
]
