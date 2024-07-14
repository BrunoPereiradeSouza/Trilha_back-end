from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm


def ProductCreateView(request):
    if request.method == 'GET':
        form = ProductForm()

    elif request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()

    return render(request, 'products/pages/form.html',
                  context={
                      'form': form
                  }
                  )


def ProductListView(request):
    products = Product.objects.all()
    return render(request, 'products/pages/index.html',
                  context={'products': products}
                  )


def ProductUpdateView(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'GET':
        form = ProductForm(instance=product)

    elif request.method == 'POST':
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'products/pages/form.html',
                  context={
                      'form': form
                  }
                  )


def ProductDeleteView(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('index')


def ProductDetailView(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/pages/product-detail.html',
                  context={
                      'product': product,
                    }
                  )
