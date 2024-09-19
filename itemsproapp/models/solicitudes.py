from typing import Any
from django.db import models

class solicitud(models.Model):
    idSold = models.AutoField(primary_key=True)
    nitSold = models.CharField(max_length=12, verbose_name="NIT")
    fecha_de_solicitud = models.DateField(verbose_name="Fecha de Solicitud")
    nombre_cliente = models.CharField(max_length=80, verbose_name="Nombre Cliente")
    nombre_edificio = models.CharField(max_length=100, verbose_name="Nombre Edificio")
    ciudad_cliente = models.CharField(max_length=40, verbose_name="Ciudad")
    direccion_cliente = models.CharField(max_length=40, verbose_name="Dirección")
    tel_admin = models.CharField(max_length=20, verbose_name="Teléfono Admin")
    correo_admin = models.EmailField(max_length=254, verbose_name="Correo Admin")

    def __str__(self):
        return f"{self.nombre_cliente} - {self.nombre_edificio}" 
