import email

from django.http import request
from django.shortcuts import redirect, render
from .models import Aluno


def cadastrar(request):
    if request.method == 'POST':
        cpf = request.POST['cpf']
        matricula = request.POST['matricula']
        nome = request.POST['nome']
        idade = request.POST.get('idade') or None
        email = request.POST['email']
        telefone = request.POST['telefone']
        endereco = request.POST['endereco']
        aluno = Aluno(cpf=cpf, matricula=matricula, nome=nome, idade=idade, email=email, telefone=telefone, endereco=endereco)
        aluno.save()
        return redirect('listar_alunos')
    return render(request, 'alunos/cadastrar.html')


def listar(request):
    alunos = Aluno.objects.all().order_by('nome')
    return render(request, 'alunos/listar.html', {'alunos': alunos})

# Create your views here.
