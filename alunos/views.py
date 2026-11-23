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
    return render(request, 'cadastrar.html')


def listar(request):
    nome = request.GET.get('nome', '').strip()
    alunos = Aluno.objects.all()
    if nome:
        alunos = alunos.filter(nome__icontains=nome)
    alunos = alunos.order_by('nome')
    return render(request, 'listar.html', {'alunos': alunos})


def pesquisar(request):
    nome = request.GET.get('nome', '').strip()
    alunos = Aluno.objects.filter(nome__icontains=nome).order_by('nome')
    return render(request, 'pesquisar.html', {'alunos': alunos, 'nome': nome})

