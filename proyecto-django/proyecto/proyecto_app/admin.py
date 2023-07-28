
from django.contrib import admin
from proyecto_app.models import *


class BarrioAdmin(admin.ModelAdmin):
    model = Barrio
    list_display = ['nombre']

admin.site.register(Barrio, BarrioAdmin)

class PersonaAdmin(admin.ModelAdmin):
    model = Persona
    list_display = ['nombre', 'apellido', 'cedula','correo']
    list_filter = ['nombre', 'apellido', 'cedula','correo']

admin.site.register(Persona, PersonaAdmin)

class LocalComidaAmdin(admin.ModelAdmin):
    model = LocalComida
    list_display = ['propietario', 'direccion', 'barrio', 'tipo_comida', 'ventas_proyectadas_mes']
    list_filter = ['propietario', 'direccion', 'barrio', 'tipo_comida', 'ventas_proyectadas_mes']

admin.site.register(LocalComida, LocalComidaAmdin)

class LocalRespuestosAdmin(admin.ModelAdmin):
    model = LocalRepuestos
    list_display = ['propietario', 'direccion', 'barrio', 'valor_total_mercaderia']
    list_filter = ['propietario', 'direccion', 'barrio', 'valor_total_mercaderia']

admin.site.register(LocalRepuestos, LocalRespuestosAdmin)