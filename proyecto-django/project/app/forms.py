from django.forms import ModelForm
from django import forms
from .models import LocalComida, LocalRepuesto, Barrio, Persona
from django.utils.translation import gettext as _

class BarrioForm(ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombre', 'siglas']
        labels = {
            'nombre':('Ingrese el nombre'),
            'siglas':('Ingrese la siglas'),
        }


class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'cedula', 'correo']
        labels = {
            'nombre':('Ingrese el nombre'),
            'apellido':('Ingrese el apellido'),
            'cedula':('Ingrese la cedula'),
            'correo':('Ingrese el correo'),
        }


class LocalComidaForm(ModelForm):
    class Meta:
        model = LocalComida
        fields = ['propietario', 'direccion', 'barrio', 'comida', 'ventas', 'permiso']
        labels = {
            'propietario': ('Ingrese el nombre'),
            'direccion': ('Ingrese la direccion'),
            'barrio': ('Seleccione  el barrio'),
            'comida': ('Ingrese el tipo de comida'),
            'ventas': ('Ingrese el valor de ventas'),
            'permiso': ('Ingrese el valor del permiso'),
        }


class LocalRepuestoForm(ModelForm):
    class Meta:
        model = LocalRepuesto
        fields = ['propietario', 'direccion', 'barrio', 'valor', 'ventas', 'permiso']
        labels = {
            'propietario': ('Ingrese el nombre'),
            'direccion': ('Ingrese la direccion'),
            'barrio': ('Seleccione el Barrio'),
            'valor': ('Ingrese el valor'),
            'ventas': ('Ingrese el valor de ventas'),
            'permiso': ('Ingrese el valor del permiso'),
        }        