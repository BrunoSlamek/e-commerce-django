from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_POST, require_GET
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('index')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'cadastrar_usuario.html', {'form_usuario': form_usuario})


@require_GET
def cadastrar_usuario(request):
    nome_usuario = request.POST['campo-nome-usuario']
    email = request.POST['campo-email']
    senha = request.POST['campo-senha'] 

    novo_usuario = User.objects.create_user(username=nome_usuario, email=email, password=senha)
    novo_usuario.save()
    return render(request, 'cadastrar_usuario.html')

