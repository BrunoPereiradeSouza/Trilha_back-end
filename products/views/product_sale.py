from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from products.models import Cart, ItemCart, Product, Sale

PER_PAGE = 12


@login_required(login_url="login")  # Só usuários logados podem acessar
def product_buy(request, id):
    # Atualiza o estoque
    product = Product.objects.get(id=id)
    product.quantity_stocked -= 1
    product.save()

    # Registra a venda
    sale = Sale.objects.create(
        product=product,
        client=request.user,
    )
    sale.save()

    messages.success(request, "Purchase was sucessfull")
    return redirect("index")


@login_required(login_url="login")
def add_to_cart(request, id):
    product = Product.objects.get(id=id)
    item, created = ItemCart.objects.get_or_create(product=product)
    if created:
        item.quantity = 1
    else:
        item.quantity += 1
    item.save()

    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart.itens.add(item)
    cart.save()
    return redirect("product", id=id)


@login_required(login_url="login")
def cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)

    return render(
        request,
        "products/pages/cart.html",
        {
            "cart": cart,
        },
    )


@login_required(login_url="login")
def cart_update(request, id):
    qtd = int(request.POST.get("quantity"))
    item = ItemCart.objects.get(id=id)
    product = Product.objects.get(id=item.product.id)
    if product.quantity_stocked >= qtd:
        item.quantity = qtd
        item.save()
        messages.success(request, "Quantity has been updated")
    else:
        messages.error(request, "Quantity not available")
    return redirect("cart")
