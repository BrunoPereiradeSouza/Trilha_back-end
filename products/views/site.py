from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_role_decorator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from products.models import Product, Sale
from products.forms import ProductForm, UserForm


@has_role_decorator("Admin")  # Define o(s) grupo(s) que pode(m) acessá-la.
def ProductCreateView(request):
    if request.method == "GET":  # Usuário acessa o form
        form = ProductForm()

    elif request.method == "POST":  # Usuário envia o form
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():  # Valida os dados enviados pelo Usuário
            form.save()
            messages.success(request, "Product was created")
            return redirect("index")

    return render(
        request,
        "products/pages/form.html",
        context={
            "form": form,
        },
    )


def ProductListView(request):  # Lista os produtos
    # Retorne o número de vendas e o faturamento total para ser exibido na home do site
    sales = Sale.objects.all()
    total, billing = 0, 0
    for sale in sales:
        total += 1
        billing += sale.product_price
    billing = f"{billing:.2f}"

    # Retorna todos os produtos salvos no Banco de Dados
    products = Product.objects.all()
    return render(
        request,
        "products/pages/index.html",
        context={
            "products": products,
            "total": total,
            "billing": billing,
        },
    )


@has_role_decorator("Admin")
def ProductUpdateView(request, id):  # Atualiza um Produto
    product = get_object_or_404(Product, id=id)

    if request.method == "GET":
        form = ProductForm(instance=product)

    elif request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            messages.success(request, "Product was updated")
            return redirect("index")

    return render(request, "products/pages/form.html", context={"form": form})


@has_role_decorator("Admin")
def ProductDeleteView(request, id):  # Deleta um Produto
    product = get_object_or_404(Product, id=id)
    product.delete()
    messages.success(request, "Product was deleted")
    return redirect("index")


def ProductDetailView(request, id):  # Detalha um Produto
    product = get_object_or_404(Product, id=id)
    return render(
        request,
        "products/pages/product-detail.html",
        context={
            "product": product,
        },
    )


@login_required(login_url="login")  # Só usuários logados podem acessar
def ProductBuyView(request, id):
    # Atualiza o estoque
    product = Product.objects.get(id=id)
    product.quantity_stocked -= 1
    product.save()

    # Registra a venda
    sale = Sale.objects.create(
        product_name=product.name,
        product_price=product.price,
        client_name=request.user.username,
    )
    sale.save()

    messages.success(request, "Purchase was sucessfull")
    return redirect("index")


def UserRegisterView(request):  # Registra um Usuário
    if request.method == "GET":
        form = UserForm()
    elif request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            # Obtem os dados enviados no form
            first_name = form.data.get("first_name")
            last_name = form.data.get("last_name")
            username = form.data.get("username")
            email = form.data.get("email")
            password = form.data.get("password")

            # Registra o Usuário atribuindo o mesmo ao grupo 'Client' criado com rolepermissions.
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
                email=email,
            )
            assign_role(user, "client")
            user.save()
            form = UserForm()
            return redirect("login")

    return render(
        request,
        "products/pages/register.html",
        context={
            "form": form,
        },
    )


def UserLoginView(request):  # Realiza o login de um Usuário no site.
    if request.method == "POST":
        # Obtem os dados enviados pelo Usuário
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Tenta autenticar o Usuário (Se não conseguir, retorna None)
        user = authenticate(username=username, password=password)

        if user:
            # Realiza o login do Usuário já autenticado.
            login(request, user)
            messages.success(request, "Sucessfully login!")
            return redirect("index")
        else:
            messages.error(request, "Invalid User or Password!")
            return redirect("login")
    else:
        return render(request, "products/pages/login.html")


@login_required(login_url="login")
def UserLogoutView(request):  # Realiza o Logout do Usuário logado no site.
    logout(request)
    messages.success(request, "you are logged out")
    return redirect("login")
