from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from products.validators import UserValidator

from .models import Product


# Form para criar e editar Produtos.
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "price",
            "category",
            "quantity_stocked",
            "cover",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control"}
            ),
            "price": forms.NumberInput(
                attrs={"class": "form-control"}
            ),
            "category": forms.Select(
                attrs={"class": "form-control"}
            ),
            "quantity_stocked": forms.NumberInput(
                attrs={"class": "form-control"}
            ),
            "cover": forms.FileInput(
                attrs={"class": "form-control"}
            ),
        }


# Form para criar Usuários e fazer login.
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "groups",
        ]
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your First Name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your last name",
                }
            ),
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your username",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your e-mail",
                }
            ),
            "password": forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your password",
                }
            ),
        }
    
    def clean(self):
        super_clean = super().clean()
        UserValidator(
            self.cleaned_data,
            ErrorClass=ValidationError,
        )
        return super_clean
