from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer

@api_view()
def ProductListApiView(request):
    products = Product.objects.all()
    serializer = ProductSerializer(instance=products, many=True)
    return Response(serializer.data)
