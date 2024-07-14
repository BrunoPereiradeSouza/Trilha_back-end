from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price',
                  'category', 'quantity_stocked',
                  'cover',
                  ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'quantity_stocked': forms.NumberInput(attrs={'class': 'form-control'}),
            'cover': forms.FileInput(attrs={'class': 'form-control'}),
        }
