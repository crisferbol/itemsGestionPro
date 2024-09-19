from django.contrib import admin
from .models import cliente
from .models import producto
from .models import solicitud




# Register your models here.

admin.site.register(cliente)
admin.site.register(producto)
admin.site.register(solicitud)
