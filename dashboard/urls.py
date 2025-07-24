from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    # URL para el dashboard del Socio
    path('socio/', views.dashboard_socio_view, name='dashboard_socio'),
    path('socio/simulador/', views.simulador_view, name='simulador'),
    path('socio/banca-virtual/', views.banca_virtual_view, name='banca_virtual'),
    path('socio/capacitacion/', views.capacitacion_view, name='capacitacion'),
    path('socio/mi-perfil/', views.mi_perfil_view, name='mi_perfil'),
    path('socio/configuracion/', views.configuracion_view, name='configuracion'),

    # URL para el dashboard del Administrador
    path('admin/', views.dashboard_admin_view, name='dashboard_admin'),
    path('admin/lista-acceso/', views.lista_acceso_view, name='lista_acceso'),
    path('admin/afiliacion/', views.afiliacion_admin_view, name='afiliacion_admin'),
    path('admin/simulador/', views.simulador_admin_view, name='simulador_admin'),
    path('admin/banca-virtual/', views.banca_virtual_admin_view, name='banca_virtual_admin'),
    path('admin/capacitacion/', views.capacitacion_admin_view, name='capacitacion_admin'),
    path('admin/noticias/', views.noticias_admin_view, name='noticias_admin'),
    path('admin/mi-perfil/', views.mi_perfil_admin_view, name='mi_perfil_admin'),
    path('admin/configuracion/', views.configuracion_admin_view, name='configuracion_admin'),
]
