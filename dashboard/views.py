from django.shortcuts import render


def dashboard_socio_view(request):
    """
    Renderiza el dashboard principal para un usuario con rol 'Socio'.
    """
    context = {
        'nombre_usuario': 'Augusto Valentino Dávila Robles',
        'foto_perfil_url': 'https://via.placeholder.com/150/f8f9fe/173d6f?text=AV'
    }
    return render(request, 'dashboard/socio/dashboardSocio.html', context)

# --- VISTAS NUEVAS PARA EL ESQUELETO ---

def simulador_view(request):
    context = {'nombre_usuario': 'Augusto Valentino Dávila Robles', 'foto_perfil_url': 'https://via.placeholder.com/150/f8f9fe/173d6f?text=AV'}
    return render(request, 'dashboard/socio/simulador.html', context)

def banca_virtual_view(request):
    context = {'nombre_usuario': 'Augusto Valentino Dávila Robles', 'foto_perfil_url': 'https://via.placeholder.com/150/f8f9fe/173d6f?text=AV'}
    return render(request, 'dashboard/socio/banca_virtual.html', context)

def capacitacion_view(request):
    context = {'nombre_usuario': 'Augusto Valentino Dávila Robles', 'foto_perfil_url': 'https://via.placeholder.com/150/f8f9fe/173d6f?text=AV'}
    return render(request, 'dashboard/socio/capacitacion.html', context)

def mi_perfil_view(request):
    context = {'nombre_usuario': 'Augusto Valentino Dávila Robles', 'foto_perfil_url': 'https://via.placeholder.com/150/f8f9fe/173d6f?text=AV'}
    return render(request, 'dashboard/socio/mi_perfil.html', context)

def configuracion_view(request):
    context = {'nombre_usuario': 'Augusto Valentino Dávila Robles', 'foto_perfil_url': 'https://via.placeholder.com/150/f8f9fe/173d6f?text=AV'}
    return render(request, 'dashboard/socio/configuracion.html', context)

# --- VISTA DEL ADMIN 

def dashboard_admin_view(request):
    context = {'nombre_usuario': 'Administrador', 'foto_perfil_url': 'https://via.placeholder.com/150/173d6f/f8f9fe?text=AD'}
    return render(request, 'dashboard/admin/dashboardAdmin.html', context)

def lista_acceso_view(request):
    context = {'nombre_usuario': 'Administrador', 'foto_perfil_url': 'https://via.placeholder.com/150/173d6f/f8f9fe?text=AD'}
    return render(request, 'dashboard/admin/lista_acceso.html', context)

def afiliacion_admin_view(request):
    context = {'nombre_usuario': 'Administrador', 'foto_perfil_url': 'https://via.placeholder.com/150/173d6f/f8f9fe?text=AD'}
    return render(request, 'dashboard/admin/afiliacion_admin.html', context)

def simulador_admin_view(request):
    context = {'nombre_usuario': 'Administrador', 'foto_perfil_url': 'https://via.placeholder.com/150/173d6f/f8f9fe?text=AD'}
    return render(request, 'dashboard/admin/simulador_admin.html', context)

def banca_virtual_admin_view(request):
    context = {'nombre_usuario': 'Administrador', 'foto_perfil_url': 'https://via.placeholder.com/150/173d6f/f8f9fe?text=AD'}
    return render(request, 'dashboard/admin/banca_virtual_admin.html', context)

def capacitacion_admin_view(request):
    context = {'nombre_usuario': 'Administrador', 'foto_perfil_url': 'https://via.placeholder.com/150/173d6f/f8f9fe?text=AD'}
    return render(request, 'dashboard/admin/capacitacion_admin.html', context)

def noticias_admin_view(request):
    context = {'nombre_usuario': 'Administrador', 'foto_perfil_url': 'https://via.placeholder.com/150/173d6f/f8f9fe?text=AD'}
    return render(request, 'dashboard/admin/noticias_admin.html', context)

def mi_perfil_admin_view(request):
    context = {'nombre_usuario': 'Administrador', 'foto_perfil_url': 'https://via.placeholder.com/150/173d6f/f8f9fe?text=AD'}
    return render(request, 'dashboard/admin/mi_perfil_admin.html', context)

def configuracion_admin_view(request):
    context = {'nombre_usuario': 'Administrador', 'foto_perfil_url': 'https://via.placeholder.com/150/173d6f/f8f9fe?text=AD'}
    return render(request, 'dashboard/admin/configuracion_admin.html', context)
