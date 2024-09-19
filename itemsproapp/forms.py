from django import forms
from .models import cliente, producto, solicitud


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
            'fecha_de_solicitud': forms.DateInput(attrs={'type': 'date'}),  # Esto agrega un calendario
        }