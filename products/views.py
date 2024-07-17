from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_role_decorator
from django.contrib.auth.models import User
from .models import Product
from .forms import ProductForm, UserForm


def ProductCreateView(request):
    if request.method == 'GET':
        form = ProductForm(request.FILES)

    elif request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Product was created')
            return redirect('index')

    return render(request, 'products/pages/form.html',
                  context={
                      'form': form,
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
            messages.success(request, 'Product was updated')
            return redirect('index')

    return render(request, 'products/pages/form.html',
                  context={
                      'form': form
                  }
                  )


def ProductDeleteView(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    messages.success(request, 'Product was deleted')
    return redirect('index')


def ProductDetailView(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/pages/product-detail.html',
                  context={
                      'product': product,
                    }
                  )


def UserCreateView(request):
    if request.method == 'GET':
        form = UserForm()
    elif request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            first_name = form.data.get('first_name')
            last_name = form.data.get('last_name')
            username = form.data.get('username')
            email = form.data.get('email')
            password = form.data.get('password')

            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
                email=email,
                )
            assign_role(user, 'client')
            user.save()

    return render(request, 'products/pages/form-client.html',
                  context={
                      'form': form,
                  })