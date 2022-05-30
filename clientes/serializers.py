from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):  
        if not cpf(data['cpf']):
            raise serializers.ValidationError({'cpf':'CPF inválido!'})
        if not nome(data['nome']):
            raise serializers.ValidationError({'nome':'Não insira números neste campo!'})
        if rg(data['rg']):
            raise serializers.ValidationError({'rg':'RG inválido, quantidade de dígitos incorreta!'})
        if not celular(data['celular']):
            raise serializers.ValidationError({'celular':'O número de telefone celular precisa conter 11 dígitos! E seguir o seguinte padrão - 99 99999-9999'})
        return data