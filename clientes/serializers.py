from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):  
        if cpf(data['cpf']):
            raise serializers.ValidationError({'cpf':'CPF inválido, quantidade de digítos incorreta!'})
        if not nome(data['nome']):
            raise serializers.ValidationError('Não insira números neste campo!')
        if rg(data['rg']):
            raise serializers.ValidationError('RG inválido, quantidade de dígitos incorreta!')
        if celular(data['celular']):
            raise serializers.ValidationError('O número de telefone celular precisa conter 11 dígitos!')
        return data