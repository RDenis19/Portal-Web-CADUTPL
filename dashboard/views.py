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


def banca_virtual_view(request):
    context = {'nombre_usuario': 'Augusto Valentino Dávila Robles',
               'foto_perfil_url': 'https://via.placeholder.com/150/f8f9fe/173d6f?text=AV'}
    return render(request, 'dashboard/socio/banca_virtual.html', context)


def capacitacion_view(request):
    context = {'nombre_usuario': 'Augusto Valentino Dávila Robles',
               'foto_perfil_url': 'https://via.placeholder.com/150/f8f9fe/173d6f?text=AV'}
    return render(request, 'dashboard/socio/capacitacion.html', context)


def mi_perfil_view(request):
    context = {'nombre_usuario': 'Augusto Valentino Dávila Robles',
               'foto_perfil_url': 'https://via.placeholder.com/150/f8f9fe/173d6f?text=AV'}
    return render(request, 'dashboard/socio/mi_perfil.html', context)


def configuracion_view(request):
    context = {'nombre_usuario': 'Augusto Valentino Dávila Robles',
               'foto_perfil_url': 'https://via.placeholder.com/150/f8f9fe/173d6f?text=AV'}
    return render(request, 'dashboard/socio/configuracion.html', context)


# --- VISTA DEL ADMIN

def dashboard_admin_view(request):
    context = {'nombre_usuario': 'Administrador',
               'foto_perfil_url': 'https://via.placeholder.com/150/173d6f/f8f9fe?text=AD'}
    return render(request, 'dashboard/admin/dashboardAdmin.html', context)


def lista_acceso_view(request):
    context = {'nombre_usuario': 'Administrador',
               'foto_perfil_url': 'https://via.placeholder.com/150/173d6f/f8f9fe?text=AD'}
    return render(request, 'dashboard/admin/lista_acceso.html', context)


def afiliacion_admin_view(request):
    context = {'nombre_usuario': 'Administrador',
               'foto_perfil_url': 'https://via.placeholder.com/150/173d6f/f8f9fe?text=AD'}
    return render(request, 'dashboard/admin/afiliacion_admin.html', context)


def simulador_admin_view(request):
    context = {'nombre_usuario': 'Administrador',
               'foto_perfil_url': 'https://via.placeholder.com/150/173d6f/f8f9fe?text=AD'}
    return render(request, 'dashboard/admin/simulador_admin.html', context)


def banca_virtual_admin_view(request):
    context = {'nombre_usuario': 'Administrador',
               'foto_perfil_url': 'https://via.placeholder.com/150/173d6f/f8f9fe?text=AD'}
    return render(request, 'dashboard/admin/banca_virtual_admin.html', context)


def capacitacion_admin_view(request):
    context = {'nombre_usuario': 'Administrador',
               'foto_perfil_url': 'https://via.placeholder.com/150/173d6f/f8f9fe?text=AD'}
    return render(request, 'dashboard/admin/capacitacion_admin.html', context)


def noticias_admin_view(request):
    context = {'nombre_usuario': 'Administrador',
               'foto_perfil_url': 'https://via.placeholder.com/150/173d6f/f8f9fe?text=AD'}
    return render(request, 'dashboard/admin/noticias_admin.html', context)


def mi_perfil_admin_view(request):
    context = {'nombre_usuario': 'Administrador',
               'foto_perfil_url': 'https://via.placeholder.com/150/173d6f/f8f9fe?text=AD'}
    return render(request, 'dashboard/admin/mi_perfil_admin.html', context)


def configuracion_admin_view(request):
    context = {'nombre_usuario': 'Administrador',
               'foto_perfil_url': 'https://via.placeholder.com/150/173d6f/f8f9fe?text=AD'}
    return render(request, 'dashboard/admin/configuracion_admin.html', context)


from decimal import Decimal, ROUND_HALF_UP

from django.shortcuts import render


# --- Lógica de Cálculo ---
# Esta sección puede ir en el mismo archivo views.py o en un archivo separado de utilidades.

def calcular_amortizacion_francesa(monto, plazo, tasa_anual):
    """Calcula la tabla de amortización por el metodo francés (cuota fija)."""
    tasa_mensual = Decimal(tasa_anual) / Decimal(12) / Decimal(100)

    # Fórmula de la cuota fija
    if tasa_mensual == 0:
        cuota = monto / plazo
    else:
        cuota = monto * (tasa_mensual * (1 + tasa_mensual) ** plazo) / ((1 + tasa_mensual) ** plazo - 1)

    cuota = cuota.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    saldo_pendiente = monto
    tabla = []
    total_intereses = Decimal(0)

    for i in range(1, plazo + 1):
        interes_mes = (saldo_pendiente * tasa_mensual).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        amortizacion_capital = cuota - interes_mes
        saldo_pendiente -= amortizacion_capital
        total_intereses += interes_mes

        # Corrección en la última cuota para que el saldo sea exactamente 0
        if i == plazo and saldo_pendiente != Decimal(0):
            amortizacion_capital += saldo_pendiente
            cuota += saldo_pendiente
            saldo_pendiente = Decimal(0)

        tabla.append({
            'periodo': i,
            'cuota': cuota,
            'interes': interes_mes,
            'amortizacion_capital': amortizacion_capital,
            'saldo_pendiente': saldo_pendiente if saldo_pendiente > 0 else 0,
        })

    return {
        'tabla_amortizacion': tabla,
        'cuota_mensual': tabla[0]['cuota'] if tabla else 0,
        'total_a_pagar': monto + total_intereses,
        'tipo_amortizacion': 'francesa'
    }


def calcular_amortizacion_alemana(monto, plazo, tasa_anual):
    """Calcula la tabla de amortización por el metodo alemán (amortización fija)."""
    tasa_mensual = Decimal(tasa_anual) / Decimal(12) / Decimal(100)
    amortizacion_fija = (monto / plazo).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    saldo_pendiente = monto
    tabla = []
    total_intereses = Decimal(0)

    for i in range(1, plazo + 1):
        interes_mes = (saldo_pendiente * tasa_mensual).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        cuota_mes = amortizacion_fija + interes_mes

        # Ajuste en la última amortización para cuadrar el monto total
        amortizacion_actual = amortizacion_fija
        if i == plazo:
            diferencia = monto - (amortizacion_fija * plazo)
            if diferencia != Decimal(0):
                amortizacion_actual += diferencia

        saldo_pendiente -= amortizacion_actual
        total_intereses += interes_mes

        tabla.append({
            'periodo': i,
            'cuota': cuota_mes,
            'interes': interes_mes,
            'amortizacion_capital': amortizacion_actual,
            'saldo_pendiente': saldo_pendiente if saldo_pendiente > 0 else 0,
        })

    return {
        'tabla_amortizacion': tabla,
        'cuota_mensual': tabla[0]['cuota'] if tabla else 0,
        'total_a_pagar': monto + total_intereses,
        'tipo_amortizacion': 'alemana'
    }


# --- Vista de Django ---

def simulador_view(request):
    # Contexto base con la información del usuario
    context = {
        'nombre_usuario': 'Augusto Valentino Dávila Robles',
        'foto_perfil_url': 'https://via.placeholder.com/150/f8f9fe/173d6f?text=AV'
    }

    # Tasas de interés (pueden venir de la base de datos en un futuro)
    TASAS_DE_INTERES = {
        'consumo': Decimal('15.0'),
        'vivienda': Decimal('9.5'),
        'vehicular': Decimal('12.0'),
    }

    if request.method == 'POST':
        # 1. Recoger datos del formulario
        tipo_credito = request.POST.get('tipo_credito')
        monto = Decimal(request.POST.get('monto', '0'))
        plazo = int(request.POST.get('plazo', '0'))
        tipo_amortizacion = request.POST.get('tipo_amortizacion')

        # 2. Obtener la tasa de interés correspondiente
        tasa_anual = TASAS_DE_INTERES.get(tipo_credito, Decimal('0'))

        # 3. Calcular según el tipo de amortización
        resultados = None
        if tipo_amortizacion == 'francesa':
            resultados = calcular_amortizacion_francesa(monto, plazo, tasa_anual)
        elif tipo_amortizacion == 'alemana':
            resultados = calcular_amortizacion_alemana(monto, plazo, tasa_anual)

        # 4. Actualizar el contexto con los resultados y los datos del formulario
        context['resultados'] = resultados
        context['form_data'] = request.POST  # Para mantener los valores en el form

    return render(request, 'dashboard/socio/simulador.html', context)
