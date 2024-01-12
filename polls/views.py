from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.urls import reverse
from .models import receita
from .forms import ReceitaForm

def index(request):
    return HttpResponse("Hello World")

def lista_receitas(request):
    receitas = receita.objects.all()
    return render(request, 'receitas/lista_receitas.html', {'receitas': receitas})

def detalhes_receita(request, receita_id):
    receita_item = get_object_or_404(receita, id=receita_id)
    return render(request, 'receitas/detalhes_receita.html', {'receita': receita_item})

def adicionar_receita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('polls:lista_receitas'))
    else:
        form = ReceitaForm()

    return render(request, 'receitas/adicionar_receita.html', {'form': form})    

def buscar_receitas(request):
    if request.method == 'GET':
        nome = request.GET.get('nome', '')
        dificuldade = request.GET.get('dificuldade', '')
        ingredientes = request.GET.get('ingredientes', '')
        tempo_preparo = request.GET.get('tempo_preparo', '')

        receitas = receita.objects.filter(
            nome__icontains=nome,
            dificuldade__icontains=dificuldade,
            ingredientes__icontains=ingredientes,
            tempo__icontains=tempo_preparo
        )

        return render(request, 'receitas/buscar_receitas.html', {'receitas': receitas})
    else:
        return render(request, 'receitas/buscar_receitas.html', {})
    
def cadastro(request):
    return render (request, 'receitas/cadastro.html', {})