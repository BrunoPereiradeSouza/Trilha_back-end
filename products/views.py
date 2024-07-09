from django.views.generic import ListView
from django.views.generic import UpdateView
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'products'
    paginate_by = 5
    ordering = ['-id']
