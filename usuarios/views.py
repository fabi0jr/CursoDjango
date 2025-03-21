from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib import messages


def login(request):
    form = LoginForms()
    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():

            nome= form["usuario"].value()
            senha = form["senha"].value()

            usuario = auth.authenticate(
                request, 
                username=nome, 
                password=senha
                )

            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f'{nome} logado com sucesso!')
                return redirect('index')
            else:
                messages.error(request, 'Usuário ou senha incorretos!')
                return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            if form["senha"].value() != form["confirmar_senha"].value():
                messages.error(request, 'Senhas não conferem!')
                return redirect('cadastro')
            
            nome = form["nome"].value()
            email = form["email"].value()
            senha = form["senha"].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Nome de usuário já existe!')
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )

            usuario.save()
            messages.success(request, f'{nome} cadastrado com sucesso!')
            return redirect('login')


    return render(request, 'usuarios/cadastro.html', {'form': form})