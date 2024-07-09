from django.contrib import admin
from .models import Category, Product 


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price',
                    'category', 'created_at', 'updated_at'
                    )
