from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

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
