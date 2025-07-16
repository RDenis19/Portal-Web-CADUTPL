from django.urls import path

from . import views

urlpatterns = [
    path('', views.login_entrada, name='login_entrada'),
    path('inicio/', views.index, name='index'),

    path('ahorros/', views.ahorros, name='ahorros'),
    path('creditos/', views.creditos, name='creditos'),
    path('servicios/', views.servicios, name='servicios'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('noticias/', views.noticias, name='noticias'),
]
