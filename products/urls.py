from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductListView, name='index'),
    path('products/<int:id>/', views.ProductDetailView, name='product'),
    path('product/create/', views.ProductCreateView, name='create'),
    path('product/update/<int:id>/', views.ProductUpdateView, name='update'),
    path('product/delete/<int:id>/', views.ProductDeleteView, name='delete'),
    path('product/buy/<int:id>/', views.ProductBuyView, name='buy'),
    path('clients/register/', views.UserRegisterView, name='register'),
    path('clients/login/', views.UserLoginView, name='login'),
    path('clients/logout/', views.UserLogoutView, name='logout'),
]
