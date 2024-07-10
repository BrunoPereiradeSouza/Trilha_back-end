from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductListView, name='index'),
    path('product/update/<int:id>/', views.ProductUpdateView, name='update'),
    path('product/delete/<int:id>', views.ProductDeleteView, name='deletar')
]
