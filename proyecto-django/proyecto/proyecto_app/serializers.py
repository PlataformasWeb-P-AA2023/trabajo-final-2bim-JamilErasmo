from rest_framework import serializers
from .models import LocalComida, LocalRepuestos, Barrio, Persona

class BarrioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barrio
        fields = '__all__'

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class LocalComidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalComida
        fields = '__all__'

class LocalRepuestosSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalRepuestos
        fields = '__all__'
