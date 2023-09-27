from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        matricula = request.POST.get('matricula')
        curso = request.POST.get('curso')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirma-senha')
        
        if any(len(field.strip()) == 0 for field in [nome, email, matricula, curso, senha, confirmar_senha]):
            return render(request, 'cadastro.html')

            
        elif senha != confirmar_senha:
            return render(request, 'cadastro.html')
        