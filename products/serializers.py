from rest_framework import serializers
from products.models import Product
from django.contrib.auth.models import User
from products.validators import UserValidator


# Classe usada para Serializar e Desserializar os Produtos
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "name", "price", "description", "category", "quantity_stocked"]

        category = serializers.StringRelatedField()


# Classe usada para Serializar e Desserializar os Usuários
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        ]
    
    def validate(self, attrs):
        super_validate = super().validate(attrs)
        UserValidator(
            data=attrs,
            ErrorClass=serializers.ValidationError,
        )
        return super_validate

    def create(self, validated_data):
        password = validated_data.pop('password')
        user  = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
