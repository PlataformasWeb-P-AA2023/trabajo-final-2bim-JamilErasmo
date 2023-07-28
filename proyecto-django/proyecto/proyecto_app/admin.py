from django.contrib import admin
from .models import Barrio, Persona, LocalComida, LocalRepuestos

# Registrar los modelos en el panel de administración
admin.site.register(Barrio)
admin.site.register(Persona)
admin.site.register(LocalComida)
admin.site.register(LocalRepuestos)
