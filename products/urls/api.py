from products import views
from rest_framework.routers import SimpleRouter


product_api_router = SimpleRouter()
product_api_router.register('products', views.ProductApiViewSet)

urlpatterns = product_api_router.urls
