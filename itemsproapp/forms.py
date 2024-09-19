from django import forms
from .models import cliente, producto, solicitud
from django.core.exceptions import ValidationError
from datetime import datetime


class clienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = '__all__'
        
class productoForm(forms.ModelForm):
    class Meta:
        model = producto
        fields = '__all__'

class solicitudForm(forms.ModelForm):
    class Meta:
        model = solicitud
        fields = '__all__'
        widgets = {
            'fecha_de_solicitud': forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}), 
        }

    def clean_fecha_de_solicitud(self):
            fecha = self.cleaned_data['fecha_de_solicitud']
            try:
                # Valida que sea en formato numérico YYYY-MM-DD
                datetime.strptime(str(fecha), '%Y-%m-%d')
            except ValueError:
                raise ValidationError("La fecha debe estar en formato YYYY-MM-DD.")
            return fecha
