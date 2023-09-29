from django.http import HttpResponse
from django.shortcuts import render
from .models import Users, Curso
from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def cadastro(request):
    if request.method == 'GET':
        cursos = Curso.objects.all()
        return render(request, 'cadastro.html', {
            'cursos': cursos
        })
    
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        nome_de_usuario = request.POST.get('nome_de_usuario')
        id_curso = request.POST.get('curso')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirma-senha')

    # TODO ADD MENSSAGES DO DJANGO
        # Verifica se o email já existe
        if Users.objects.filter(email=email).exists():
            return HttpResponse('Email já existe')

        # Verifica se o nome de usuário já existe
        elif Users.objects.filter(username=nome_de_usuario).exists():
            return HttpResponse('Nome de usuário já existe')
        
        elif any(len(field.strip()) == 0 for field in [nome, email, nome_de_usuario, id_curso, senha, confirmar_senha]):
            return render(request, 'cadastro.html')

            
        elif senha != confirmar_senha:
            return render(request, 'cadastro.html')
        
        curso = Curso.objects.get(id=id_curso)

        Users.objects.create_user(username=nome_de_usuario, email=email, password=senha, curso=curso, nome=nome)

        return HttpResponse(f"Usuário(a) {nome} do curso {curso} cadastrado(a) com sucesso!")

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    
    elif request.method == 'POST':

        user = authenticate(

            request, username = request.POST['nome-de-usuario'], password = request.POST['senha']

        )

        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm,
                'error': 'Usuário e/ou senha incorreto!' 
            })
        
        else:
            login_django(request, user)
            return HttpResponse('Logado com sucesso!')


    