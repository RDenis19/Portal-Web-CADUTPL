from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # URL para el dashboard del Socio
    path('socio/', views.dashboard_socio_view, name='dashboard_socio'),
    
    # URL para el dashboard del Administrador
    path('admin/', views.dashboard_admin_view, name='dashboard_admin'),
]
