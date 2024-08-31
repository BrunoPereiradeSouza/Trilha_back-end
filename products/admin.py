from django.contrib import admin

from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "price",
        "category",
        "created_at",
        "updated_at",
    )


@admin.register(models.Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ("product_name", "product_price", "client_username")

    def product_name(self, obj):
        return obj.product.name

    product_name.admin_order_field = "product__name"
    product_name.short_description = "Product Name"

    def product_price(self, obj):
        return obj.product.price

    product_name.admin_order_field = "product__price"
    product_name.short_description = "Product Name"

    def client_username(self, obj):
        return obj.client.username

    client_username.admin_order_field = "client__username"
    client_username.short_description = "Client Username"


admin.site.register(models.ItemCart)
admin.site.register(models.Cart)
