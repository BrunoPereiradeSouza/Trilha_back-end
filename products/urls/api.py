from products import views
from django.urls import path
from rest_framework.routers import SimpleRouter


# Cria um router
product_api_router = SimpleRouter()

# Registra o router
product_api_router.register("products", views.ProductApiViewSet)

urlpatterns = [
    path(
        "client/register/", views.UserApiRegister.as_view(), name="client_api_register"
    ),
]

# Adiciona o router nas urlpatterns
urlpatterns += product_api_router.urls
