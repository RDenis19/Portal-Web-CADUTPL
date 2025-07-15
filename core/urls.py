from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),

    path('inicio/', views.index, name='index'),

    # URLs para el resto de las páginas
    path('ahorros/', views.ahorros, name='ahorros'),
    path('creditos/', views.creditos, name='creditos'),
    path('servicios/', views.servicios, name='servicios'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('noticias/', views.noticias, name='noticias'),
    path('hazte-socio/', views.haste_socio, name='haste_socio'),
    path('ingreso/', views.login_ingreso, name='login_ingreso'),
]
