from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from products.models import Product
from django.contrib.auth.models import User
from products.serializers import ProductSerializer, UserSerializer


# Realiza o CRUD dos Produtos.
class ProductApiViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Registra um usuário no Banco de Dados.
class UserApiRegister(CreateAPIView):
    serializer_class = UserSerializer

