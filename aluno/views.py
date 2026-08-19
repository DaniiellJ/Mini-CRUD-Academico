from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno
from .forms import AlunoForm

# Create your views here.

def lista_aluno(request):
    # Sorting support via ?sort=<option>
    # Options: id_asc, id_desc, nome_asc, nome_desc (default: nome_asc)
    sort = request.GET.get('sort', 'nome_asc')

    if sort == 'id_desc':
        alunos = Aluno.objects.all().order_by('-id')
        id_sort = 'id_asc'
        nome_sort = 'nome_asc'
    elif sort == 'id_asc':
        alunos = Aluno.objects.all().order_by('id')
        id_sort = 'id_desc'
        nome_sort = 'nome_asc'
    elif sort == 'nome_desc':
        alunos = Aluno.objects.all().order_by('-nome')
        nome_sort = 'nome_asc'
        id_sort = 'id_asc'
    else:
        # nome_asc default
        alunos = Aluno.objects.all().order_by('nome')
        nome_sort = 'nome_desc'
        id_sort = 'id_asc'

    return render(
        request,
        'aluno/lista.html',
        {'alunos': alunos, 'current_sort': sort, 'id_sort': id_sort, 'nome_sort': nome_sort}
    )

def detalhe_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)

    return render(
        request,
        'aluno/detalhe.html',
        {'aluno': aluno}
    )

def criar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alunos')
    else:
        form = AlunoForm()

    return render(request, 'aluno/form.html', {'form': form})


def editar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)

    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('detalhe_aluno', id=aluno.id)
    else:
        form = AlunoForm(instance=aluno)

    return render(
        request,
        'aluno/form.html',
        {'form': form, 'aluno': aluno}
    )


def excluir_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)

    if request.method == 'POST':
        aluno.delete()

        return redirect('lista_alunos')

    return render(
        request,
        'aluno/exclusao.html',
        {'aluno': aluno}
    )
