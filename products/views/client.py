from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from rolepermissions.roles import assign_role

from products.forms import UserForm

PER_PAGE = 12


def client_register(request):
    if request.method == "GET":
        form = UserForm()

    elif request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            # Obtem os dados enviados no form
            data = form.cleaned_data

            # Atribui o usuário ao grupo 'client'
            user = User.objects.create_user(
                first_name=data["first_name"],
                last_name=data["last_name"],
                username=data["username"],
                email=data["email"],
                password=data["password"],
        )

        assign_role(user, "client")
        form = UserForm()
        messages.success(
            request, 
            "Create user was sucessfull"
        )
        return redirect("login")

    return render(
        request,
        "products/pages/register.html",
        context={
            "form": form,
        },
    )


def client_login(request): 

    if request.method == "POST":
        # Obtem os dados enviados pelo Usuário
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Tenta autenticar o Usuário (Se não conseguir, retorna None)
        user = authenticate(
            username=username, 
            password=password
        )

        if user:
            # Realiza o login do Usuário já autenticado.
            login(request, user)
            messages.success(
                request, 
                "Sucessfully login!"
            )
            return redirect("index")
        else:
            messages.error(
                request, 
                "Invalid User or Password!"
            )
            return redirect("login")

    return render(
        request, 
        "products/pages/login.html"
    )


@login_required(login_url="login")
def client_logout(request): 
    logout(request)
    messages.success(request, "you are logged out")
    return redirect("login")
