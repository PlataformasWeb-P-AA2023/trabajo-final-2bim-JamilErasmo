from django.db import models

# Definir el modelo Barrio
class Barrio(models.Model):
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

# Definir el modelo Persona
class Persona(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=10, unique=True)
    correo = models.EmailField()

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

# Definir el modelo LocalComida
class LocalComida(models.Model):
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=200)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)
    tipo_comida = models.CharField(max_length=100)
    ventas_proyectadas = models.DecimalField(max_digits=10, decimal_places=2)
    pago_permiso = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.pago_permiso = self.ventas_proyectadas * 0.8
        super(LocalComida, self).save(*args, **kwargs)

    def __str__(self):
        return f"Local de Comida - {self.propietario} - {self.tipo_comida}"

# Definir el modelo LocalRepuestos
class LocalRepuestos(models.Model):
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=200)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)
    valor_mercaderia = models.DecimalField(max_digits=10, decimal_places=2)
    valor_pago_permiso = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.valor_pago_permiso = self.valor_mercaderia * 0.001
        super(LocalRepuestos, self).save(*args, **kwargs)

    def __str__(self):
        return f"Local de Repuestos - {self.propietario}"

