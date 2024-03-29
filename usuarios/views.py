from django.http import HttpResponse
from django.shortcuts import render
from .models import Users, Curso
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.messages import constants


# Create your views here.
def cadastro(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'GET':
        cursos = Curso.objects.all()
        return render(request, 'cadastro.html', {
            'cursos': cursos
        })
    
    elif request.method == 'POST':
        cursos = Curso.objects.all()

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        nome_de_usuario = request.POST.get('nome_de_usuario')
        id_curso = request.POST.get('curso')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirma-senha')

    # TODO ADD MENSSAGES DO DJANGO
        # Verifica se o email já existe
        if Users.objects.filter(email=email).exists():
            messages.add_message(request, constants.ERROR, 'Email já existe')
            
            return render(request, 'cadastro.html', {
                'form': AuthenticationForm,
                'cursos': cursos
            })

        # Verifica se o nome de usuário já existe
        elif Users.objects.filter(username=nome_de_usuario).exists():
            messages.add_message(request, constants.ERROR, 'Nome de usuário já existe')
            return render(request, 'cadastro.html', {
                'form': AuthenticationForm,
                'cursos': cursos
            })
        
        elif any(len(field.strip()) == 0 for field in [nome, email, nome_de_usuario, id_curso, senha, confirmar_senha]):
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return render(request, 'cadastro.html', {
                'form': AuthenticationForm,
                'cursos': cursos
            })

            
        elif senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Senhas não coincidem')
            return render(request, 'cadastro.html', {
                'form': AuthenticationForm,
                'cursos': cursos
            })
        
        
        curso = Curso.objects.get(id=id_curso)

        try:
            Users.objects.create_user(username=nome_de_usuario, email=email, password=senha, curso=curso, nome=nome)
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso')
            return render(request, 'cadastro.html', {
                'form': AuthenticationForm,
                'cursos': cursos
            } )
        except:
            messages.add_message(request, constants.WARNING, 'Erro interno, tente novamente mais tarde')
            return render(request, 'cadastro.html', {
                'form': AuthenticationForm,
                'cursos': cursos
            })
        
def entrar(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'GET':
        return render(request,'login.html')
    
    elif request.method == 'POST':

        user = authenticate(

            request, username = request.POST['nome-de-usuario'], password = request.POST['senha']

        )

        if user is None:
            messages.add_message(request, constants.ERROR, 'Usuário e/ou senha incorreto!')
            return render(request, 'login.html')
        
        else:
            login(request, user)
            return redirect('/')


def sair(request):
    logout(request)
    return redirect('/auth/entrar')
