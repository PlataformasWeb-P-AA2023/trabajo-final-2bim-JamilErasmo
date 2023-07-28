from django import forms
from .models import Persona, Barrio, LocalComida, LocalRepuestos

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'otro_campo']  # Agrega otros campos que desees incluir en el formulario

class BarrioForm(forms.ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombre']

class LocalComidaForm(forms.ModelForm):
    class Meta:
        model = LocalComida
        fields = ['propietario', 'direccion', 'barrio', 'tipo_comida', 'ventas_proyectadas_mes']

class LocalRespuestosForm(forms.ModelForm):
    class Meta:
        model = LocalRepuestos
        fields = ['propietario', 'direccion', 'barrio', 'valor_total_mercaderia']
