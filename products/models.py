from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity_stocked = models.IntegerField()
    cover = models.ImageField(
        upload_to="products/covers/%Y/%m/%d/", blank=True, default=""
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Carrinho de {self.user.username}"

    def get_cart_total_value(self):
        return sum(item.get_total_value() for item in self.itens.all())

class ItemCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name

    def total_value(self):
        return self.quantity * self.product.price
