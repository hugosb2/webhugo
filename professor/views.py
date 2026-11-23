from django.http import request
from django.shortcuts import redirect, render
from .models import Professor

def listar(request):
    professores = Professor.objects.all().order_by('nome')
    return render(request, 'professor/listar.html', {'professores': professores})

def cadastrar(request):
    if request.method == 'POST':
        cpf = request.POST['cpf']
        nome = request.POST['nome']
        idade = int(request.POST['idade'])
        email = request.POST['email']
        siape = request.POST['siape']
        telefone = request.POST['telefone']
        endereco = request.POST['endereco']

        professor = Professor(cpf=cpf, nome=nome, idade = idade, email = email, siape = siape, telefone = telefone, endereco = endereco)
        professor.save()
        return redirect('cadastrar_professor')

    return render(request, 'professor/cadastrar.html')