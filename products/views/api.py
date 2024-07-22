from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from products.models import Product, Sale
from products.serializers import ProductSerializer, UserSerializer


# Realiza o CRUD dos Produtos.
class ProductApiViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


# Registra um usuário no Banco de Dados.
class UserApiRegister(CreateAPIView):
    serializer_class = UserSerializer


@api_view()
@permission_classes([IsAdminUser])
def BillingApiView(request):
    sales = Sale.objects.all()
    total_billing, sales_number = 0, 0
    for sale in sales:
        total_billing += sale.product.price
        sales_number += 1
    return Response({
        "Total Billing": total_billing,
        "Sales Number": sales_number,
    })
