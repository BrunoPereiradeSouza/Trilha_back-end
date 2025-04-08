from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from rolepermissions.decorators import has_role_decorator

from products.forms import ProductForm
from products.models import Product, Sale
from products.utils.pagination import make_pagination

PER_PAGE = 12

def home(request):
    # Retorna o número de vendas e o faturamento total
    sales = Sale.objects.all()
    sales_number = sales.count()
    billing = 0

    if sales.count() > 0:
        for sale in sales:
            billing += sale.product.price
        billing = f"{billing:.2f}"

    # Retorna todos os produtos com estoque disponível
    products = Product.objects.filter(
        quantity_stocked__gt=0
    ).order_by("-id")

    # Paginação
    page_obj, pagination = make_pagination(products, PER_PAGE, request)

    return render(
        request,
        "products/pages/index.html",
        context={
            "products": page_obj,
            "pagination": pagination,
            "total": sales_number,
            "billing": billing,
        },
    )


@has_role_decorator("Admin")  
def product_create(request):
    if request.method == "GET": 
        form = ProductForm()

    elif request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid(): 
            form.save()
            messages.success(
                request, 
                "Product was created"
            )
            return redirect("index")

    return render(
        request,
        "products/pages/form.html",
        context={
            "form": form,
        },
    )


@has_role_decorator("Admin")
def product_update(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "GET":
        form = ProductForm(instance=product)

    elif request.method == "POST":
        form = ProductForm(
            request.POST, 
            request.FILES, 
            instance=product
    )

        if form.is_valid():
            form.save()
            messages.success(
                request, 
                "Product was updated"
            )
            return redirect("index")

    return render(
        request, 
        "products/pages/form.html", 
        context={"form": form}
    )


@has_role_decorator("Admin")
def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    messages.success(request, "Product was deleted")
    return redirect("index")


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(
        request,
        "products/pages/product-detail.html",
        context={
            "product": product,
            "is_detail_page": True,
        },
    )
