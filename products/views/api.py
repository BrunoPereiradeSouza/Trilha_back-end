from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from products.models import Product
from products.serializers import ProductSerializer, UserSerializer


# Realiza o CRUD dos Produtos.
class ProductApiViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


# Registra um usuário no Banco de Dados.
class UserApiRegister(CreateAPIView):
    serializer_class = UserSerializer
