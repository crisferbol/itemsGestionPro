from typing import Any
from django.db import models

# Create your models here. id nit nomb.edificio dir tel correo

class cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nit = models.CharField(max_length=12, verbose_name="NIT.")
    nombreEdificio = models.CharField(max_length=80, verbose_name="Nombre Edificio")
    dirEdificio = models.CharField(max_length=100, verbose_name="Dirección Edificio")
    telAdmon = models.CharField(max_length=10, verbose_name="Teléfono Admón")
    correoAdmon = models.CharField(max_length=100, verbose_name="Correo Admón")
    
    def __str__(self):
        return f"{self.nombreEdificio} - {self.nit}"
    

