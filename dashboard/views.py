from django.shortcuts import render

def dashboard_socio_view(request):
    """
    Renderiza el dashboard principal para un usuario con rol 'Socio'.
    """
    # Aquí el backend developer puede añadir lógica para obtener datos del socio
    context = {
        'nombre_usuario': 'Augusto Valentino Dávila Robles', # Dato de ejemplo
        'foto_perfil_url': 'https://via.placeholder.com/150' # URL de ejemplo
    }
    return render(request, 'dashboard/socio/dashboardSocio.html', context)


def dashboard_admin_view(request):
    """
    Renderiza el dashboard principal para un usuario con rol 'Administrador'.
    """
    # Aquí el backend developer puede añadir lógica para obtener datos del admin
    context = {
        'nombre_usuario': 'Administrador del Sistema', # Dato de ejemplo
        'foto_perfil_url': 'https://via.placeholder.com/150' # URL de ejemplo
    }
    return render(request, 'dashboard/admin/dashboardAdmin.html', context)
