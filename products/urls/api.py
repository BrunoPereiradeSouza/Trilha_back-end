from django.urls import path
from products import views

urlpatterns = [
    path('products/', views.ProductListApiView, name='api_products_list'),
]
