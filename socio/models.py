from django.db import models


def solicitud_socio_upload_path(instance, filename):
    """Genera la ruta de subida para los documentos de solicitud de socio."""
    return f'socios/solicitudes/{instance.cedula}/{filename}'


class SolicitudSocio(models.Model):
    # Datos personales
    cedula = models.CharField(max_length=10, unique=True, verbose_name="Cédula")
    nombres = models.CharField(max_length=100, verbose_name="Nombres")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    celular = models.CharField(max_length=15, verbose_name="Celular")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")

    # Documentos adjuntos
    solicitud_ingreso = models.FileField(
        upload_to=solicitud_socio_upload_path,
        verbose_name="Solicitud de Ingreso"
    )
    designacion_beneficiario = models.FileField(
        upload_to=solicitud_socio_upload_path,
        verbose_name="Designación de Beneficiario"
    )
    autorizacion_descuento = models.FileField(
        upload_to=solicitud_socio_upload_path,
        verbose_name="Autorización de Descuento"
    )

    # Campos de seguimiento
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ESTADOS = (
        ('PENDIENTE', 'Pendiente'),
        ('APROBADO', 'Aprobado'),
        ('RECHAZADO', 'Rechazado'),
    )
    estado = models.CharField(max_length=10, choices=ESTADOS, default='PENDIENTE')

    def __str__(self):
        return f"Solicitud de {self.nombres} {self.apellidos} ({self.cedula})"

    class Meta:
        verbose_name = "Solicitud de Socio"
        verbose_name_plural = "Solicitudes de Socios"
