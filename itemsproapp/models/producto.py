from typing import Any
from django.db import models
import logging

logger = logging.getLogger(__name__)

class producto(models.Model):  
    idProd = models.AutoField(primary_key=True)
    nombreProd = models.CharField(max_length=20, verbose_name="Descripcion del Producto")
    modeloProd = models.CharField(max_length=50, verbose_name="Modelo del Producto", default='')
    fotoProd = models.ImageField(upload_to='img/', verbose_name="Foto Producto", null=True)
    marcaProd = models.CharField(max_length=80, verbose_name="Marca Camara") 
    
    def __str__(self):
        return f"{self.nombreProd} - {self.marcaProd}" 
    
    def delete(self, using=None, keep_parents=False):
        self.fotoProd.storage.delete(self.fotoProd.name)
        super().delete()