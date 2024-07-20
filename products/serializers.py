from rest_framework import serializers
from products.models import Product
from django.contrib.auth.models import User


# Classe usada para Serializar e Desserializar os Produtos
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'category', 'quantity_stocked']

        category = serializers.StringRelatedField()


# Classe usada para Serializar e Desserializar os Usuários
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username', 'email', 'password',
            ]
