
from django.db import models

# Create your models here.
class Barrio(models.Model):
    nombre = models.CharField(max_length=100)

    def _str_(self):
        return self.nombre


class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.IntegerField()
    correo = models.CharField(max_length=20)

    def _str_(self):
        return "%s %s - Cédula: %d - Correo: %s" % (self.nombre, self.apellido, self.cedula, self.correo)


class LocalComida(models.Model):
    ventas_proyectadas_mes = models.FloatField()
    tipo_comida = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    propietario = models.CharField(max_length=100)
    barrio = models.CharField(max_length=100)

class LocalRepuestos(models.Model):
    # ... (el resto de tu código)
    
    def _str_(self):
        return "%s - %s - %s - %.2f" % (self.propietario, self.direccion, self.barrio, self.valor_total_mercaderia)

