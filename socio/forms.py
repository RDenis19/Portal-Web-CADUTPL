from django import forms

from .models import SolicitudSocio


class SolicitudSocioForm(forms.ModelForm):
    class Meta:
        model = SolicitudSocio
        fields = [
            'cedula', 'nombres', 'apellidos', 'celular', 'email',
            'solicitud_ingreso', 'designacion_beneficiario', 'autorizacion_descuento'
        ]
