from django.urls import path

from products import views

urlpatterns = [
    path("", views.product_list, name="index"),
    path("products/<int:id>/", views.product_detail, name="product"),
    path("product/create/", views.product_create, name="create"),
    path("product/update/<int:id>/", views.product_update, name="update"),
    path("product/delete/<int:id>/", views.product_delete, name="delete"),
    path("product/buy/<int:id>/", views.product_buy, name="buy"),
    path("clients/register/", views.client_register, name="register"),
    path("clients/login/", views.client_login, name="login"),
    path("clients/logout/", views.client_logout, name="logout"),
    path("cart/product/<int:id>/", views.add_to_cart, name="add_to_cart"),
]
