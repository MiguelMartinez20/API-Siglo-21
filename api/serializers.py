from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = (
            'run',
            'nombre',
            'telefono',
            'email',
            'reserva',
        )