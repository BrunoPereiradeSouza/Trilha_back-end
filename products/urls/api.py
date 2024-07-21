from products import views
from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


# Cria um router
product_api_router = SimpleRouter()

# Registra o router
product_api_router.register("products", views.ProductApiViewSet)

urlpatterns = [
    path(
        "client/register/", views.UserApiRegister.as_view(), name="client_api_register",
    ),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

# Adiciona o router nas urlpatterns
urlpatterns += product_api_router.urls
