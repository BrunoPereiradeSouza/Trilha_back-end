from django.urls import path

from products import views

urlpatterns = [
    path("", views.home, name="index"),
    path("products/<int:id>/", views.product_detail, name="product"),
    path("product/create/", views.product_create, name="create"),
    path("product/update/<int:id>/", views.product_update, name="update"),
    path("product/delete/<int:id>/", views.product_delete, name="delete"),
    path("product/buy/<int:id>/", views.product_buy, name="buy"),
    path("clients/register/", views.client_register, name="register"),
    path("clients/login/", views.client_login, name="login"),
    path("clients/logout/", views.client_logout, name="logout"),
    path("cart/product/<int:id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.cart, name="cart"),
    path("cart/update/<int:id>/", views.cart_update, name="cart_update"),
    path("cart/delete/<int:id>/", views.remove_to_cart, name="remove_to_cart"),
    path("cart/buy/", views.cart_buy, name="cart_buy"),
]
